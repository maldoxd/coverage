import statistics
import fastapi
from app.integrations.connect_apis import get_coverage
from app.models.coverage import Coverage
from statistics import mode

router = fastapi.APIRouter()

@router.get("/members/{member_id}")
def coalesce_coverages(member_id: int):
    try:
        coverages = get_coverage(member_id)
        if len(coverages) == 0: #For simplicity I'm assuming that if all APIs return no data, the member is not found, but I recognize it could be all APIs are down
            #assuming that the member is not found if we don't get any coverages from the APIs
            raise fastapi.HTTPException(status_code=404, detail="Member not found")
        else:
            return coalesce(coverages)
    except fastapi.HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        print(f"Error while getting coverage for member {member_id}: {e}")
        raise fastapi.HTTPException(status_code=500, detail="Internal server error")

def coalesce(coverages):
    try:
        mode_oop_max = mode(coverage.oop_max for coverage in coverages if coverage.oop_max != 0)
        mode_remaining_oop_max = mode(coverage.remaining_oop_max for coverage in coverages if coverage.remaining_oop_max != 0)
        mode_copay = mode(coverage.copay for coverage in coverages if coverage.copay != 0)

        return Coverage(oop_max=mode_oop_max, remaining_oop_max=mode_remaining_oop_max, copay=mode_copay)
    except statistics.StatisticsError:
        #assuming that if there is no unique mode, we cannot determine the coverage, raising message
        print("No unique mode found")
        raise fastapi.HTTPException(status_code=400, detail="Cannot determine coverage at this time. Call you provider.")
    
