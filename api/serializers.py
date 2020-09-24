from rest_framework import serializers, filters

from .models import *

class DataListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OverviewData
        fields = ('id', 'name', 'status', 'category', 'submit_type', 
        'description', 'premium_total', 'premium_total_com', 
        'premium_total_auth', 'premium_percent_com', 
        'premium_percent_auth', 'dwp', 
        'premium_growth_actual','premium_growth_target','policy_count_actual','policy_count_target',
        'dwp_per_policy_actual','dwp_per_policy_target','loss_ratio_actual','loss_ratio_target',
        'loss_ratio_cat_actual','loss_ratio_cat_target','loss_ratio_large_actual','loss_ratio_large_target', 
        'claim_count_actual','claim_count_target','loss_size_avg_actual','loss_size_avg_target', 
        'commodity_count_total','commodity_dwp_percent','submission_count_total','submission_dwp_percent')

class AlertListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlertData
        fields = ('id', 'name', 'data', 'description', 'data', 'recommendation', 
        'recommendation_desc', 'alert_date', 'created_date', 'created_by', 'condition', 
        'amount', 'reviewer', 'involved', 'action_taken', 'completed_date', 'status')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentData
        fields = ('id', 'subject', 'content', 'data', 'created_date', 'created_by', 'topic')

class PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PolicyData
        fields = ('id', 'subject', 'content', 'policy_nb', 'created_date', 'created_by', 'topic')





