from fastapi import FastAPI
from API.routers.vehicles import vehicle

from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html


def swagger_monkey_patch(*args, **kwargs):
    """
    Wrap the function which is generating the HTML for the /docs endpoint and
    overwrite the default values for the swagger js and css.
    """
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui.css")


# Actual monkey patch
applications.get_swagger_ui_html = swagger_monkey_patch


vehicleAPI = FastAPI()
vehicleAPI.include_router(vehicle)

@vehicle.on_event("startup")
async def startup():
    # engine = create_engine(POSTGRES_URI)
    # Session = sessionmaker(bind=engine)
    # DBSession = Session()
    # response = DBSession.query(vehicle_control).all()
    print("Database connected!")

