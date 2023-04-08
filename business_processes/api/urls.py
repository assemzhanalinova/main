from rest_framework import routers

from business_processes.api.viewset import (
    BusinessProcessAsIsViewSet,
    BusinessProcessToBeViewSet,
)

router = routers.SimpleRouter()
router.register("as-is", BusinessProcessAsIsViewSet)
router.register("to-be", BusinessProcessToBeViewSet)

urlpatterns = router.urls
