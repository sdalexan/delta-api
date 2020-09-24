from rest_framework import viewsets
from .serializers import *
from .models import *


class AlertListViewSet(viewsets.ModelViewSet):
    serializer_class = AlertListSerializer
    queryset = AlertData.objects.all().order_by('id')
    def get_queryset(self):
        id = self.request.query_params.get('id')
        category = self.request.query_params.get('category')
        if id:
            return AlertData.objects.filter(data__id=id)
        if category:
            return AlertData.objects.filter(data__category=category)
        return AlertData.objects.all()


class DataListViewSet(viewsets.ModelViewSet):
    queryset = OverviewData.objects.filter().order_by('id')
    serializer_class = DataListSerializer
    def get_queryset(self):
        if self.request.query_params.get('name'):
            name = str(self.request.query_params.get('name'))
            return OverviewData.objects.filter(name=name)
        if self.request.query_params.get('category'):
            category = str(self.request.query_params.get('category')).lower()
            return OverviewData.objects.filter(category=category)
        if self.request.query_params.get('submit_type'):
            submit_type = str(self.request.query_params.get('submit_type')).lower()
            return OverviewData.objects.filter(submit_type=submit_type)
        return OverviewData.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentData.objects.all().order_by('id')
    serializer_class = CommentSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id')
        if id:
            return CommentData.objects.filter(data__id=id)
        return CommentData.objects.all()

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = PolicyData.objects.all().order_by('id')
    serializer_class = PolicySerializer
# class SegmentOverviewViewSet(viewsets.ModelViewSet):
#     queryset = OverviewData.objects.filter(category="segment").order_by('id')
#     serializer_class = SegmentOverviewSerializer

# class SegmentListViewSet(viewsets.ModelViewSet):
#     queryset = OverviewData.objects.filter(category="segment").order_by('id')
#     serializer_class = DataListSerializer

# class AgentListViewSet(viewsets.ModelViewSet):
#     queryset = OverviewData.objects.filter(category="agent").order_by('id')
#     serializer_class = DataListSerializer

# class StateListViewSet(viewsets.ModelViewSet):
#     queryset = OverviewData.objects.filter(category="state").order_by('id')
#     serializer_class = DataListSerializer

# class ProgramListViewSet(viewsets.ModelViewSet):
#     queryset = OverviewData.objects.filter(category="program").order_by('id')
#     serializer_class = DataListSerializer



# class DescriptionViewSet(viewsets.ModelViewSet):
#    queryset = OverviewData.objects.all()
#    serializer_class = DescriptionSerializer

#    def get_queryset(self):
#         qs = super().get_queryset()
#         name = str(self.request.query_params.get('name')).lower()
#         return OverviewData.objects.filter(id=name)

# class AlertSearchViewSet(viewsets.ModelViewSet):
#    queryset = AlertData.objects.all()
#    serializer_class = AlertListSerializer

#    def get_queryset(self):
#         qs = super().get_queryset()
#         name = str(self.request.query_params.get('data')).lower()
#         return AlertData.objects.filter(data__name=name)



    






# class SegmentAlertViewSet(viewsets.ModelViewSet):
#     queryset = SegmentAlert.objects.all().order_by('id')
#     serializer_class = SegmentAlertSerializer


# class AgentCommentViewSet(viewsets.ModelViewSet):
#     queryset = AgentComment.objects.all().order_by('id')
#     serializer_class = AgentCommentSerializer



