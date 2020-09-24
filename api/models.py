from django.db import models

# Create your models here.

#Information and Metrics for Agent, State, Program, and Segment
class OverviewData(models.Model):
    def __str__(self):
       return f"{self.category} - {self.name}"
    class Meta:
        verbose_name_plural = "Data"
    name = models.CharField(max_length = 50,verbose_name = "Name")
    category = models.CharField(max_length = 50,verbose_name = "Category", blank=True)
    submit_type = models.CharField(max_length = 50,verbose_name = "Submit Type", blank=True)
    description = models.TextField(verbose_name = "Description", blank=True)
    premium_total = models.IntegerField(default=0, blank=True, verbose_name = "Premium Total")
    premium_total_auth = models.IntegerField(verbose_name = "Authority Premium Total", default=0, blank=True)
    premium_total_com = models.IntegerField(verbose_name = "Commodity Premium Total", default=0, blank=True)
    premium_percent_auth = models.IntegerField(verbose_name = "Authority Premium Percent", default=0, blank=True)
    premium_percent_com = models.IntegerField(verbose_name = "Commodity Premium Percent", default=0, blank=True)
    dwp = models.IntegerField(verbose_name = "Direct Written Premium", default=0, blank=True)
   # updated_date = models.DateTimeField(auto_now=True)

    #KPI Fields used in CSF Panel
    status = models.CharField(max_length = 10, verbose_name = "Status", blank=True)

    premium_growth_actual = models.IntegerField(verbose_name = "Actual Premium Growth", default=0, blank=True)
    premium_growth_target = models.IntegerField(verbose_name = "Target Premium Growth", default=0, blank=True)

    policy_count_actual = models.IntegerField(verbose_name = "Actual Inforce Policy Count", default=0, blank=True)
    policy_count_target = models.IntegerField(verbose_name = "Target Inforce Policy Count", default=0, blank=True)

    dwp_per_policy_actual = models.IntegerField(verbose_name = "Actual Dwp Per In-Force Policy", default=0, blank=True)
    dwp_per_policy_target = models.IntegerField(verbose_name = "Target Dwp Per In-Force Policy", default=0, blank=True)

    loss_ratio_actual = models.IntegerField(verbose_name = "Actual Loss Ratio Non-CAT", default=0, blank=True)
    loss_ratio_target = models.IntegerField(verbose_name = "Actual Loss Ratio Non-CAT", default=0, blank=True)

    loss_ratio_cat_actual = models.IntegerField(verbose_name = "Actual Loss Ratio CAT", default=0, blank=True)
    loss_ratio_cat_target = models.IntegerField(verbose_name = "Target Loss Ratio CAT", default=0, blank=True)

    loss_ratio_large_actual = models.IntegerField(verbose_name = "Actual Loss Ratio Large Loss", default=0, blank=True)
    loss_ratio_large_target = models.IntegerField(verbose_name = "Targe Loss Ratio Large Loss", default=0, blank=True)

    claim_count_actual = models.IntegerField(verbose_name = "Actual Claim Count", default=0, blank=True)
    claim_count_target = models.IntegerField(verbose_name = "Target Claim Count", default=0, blank=True)

    loss_size_avg_actual = models.IntegerField(verbose_name = "Actual Average Loss Size", default=0, blank=True)
    loss_size_avg_target = models.IntegerField(verbose_name = "Target Average Loss Size", default=0, blank=True)

    commodity_count_total = models.IntegerField(verbose_name = "Commodity Count", default=0, blank=True)
    commodity_dwp_percent = models.IntegerField(verbose_name = "Commodity DWP Percent", default=0, blank=True)
    submission_count_total = models.IntegerField(verbose_name = "Submission Count", default=0, blank=True)
    submission_dwp_percent = models.IntegerField(verbose_name = "Submission DWP Percent", default=0, blank=True)



class AlertData(models.Model):
    def __str__(self):
       return f"{self.name} - {self.description}"
    class Meta:
        verbose_name_plural = "Alerts"
    name = models.CharField(max_length = 50, verbose_name = "Alert Name")
    description = models.TextField(verbose_name = "Alert Description", blank=True, null=True)
    data = models.ForeignKey(OverviewData, on_delete=models.CASCADE, verbose_name = "Targe Data")
    recommendation = models.CharField(max_length = 50, verbose_name = "Recommendation", blank=True, null=True)
    recommendation_desc = models.TextField(verbose_name = "Recommendation Description", blank=True, null=True)
    alert_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name = "Alert Date", null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name = "Created Date")
    created_by = models.CharField(max_length = 50,verbose_name = "Created By")
    condition = models.CharField(max_length = 50,verbose_name = "Operation", blank=True, null=True)
    amount = models.IntegerField(verbose_name = "amount")
    reviewer = models.CharField(max_length = 50,verbose_name = "Reviewer", blank=True, null=True)
    involved = models.CharField(max_length = 50,verbose_name = "Others Involved", blank=True, null=True)
    action_taken = models.TextField(verbose_name = "Action Taken", blank=True, null=True)
    completed_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name = "Created Date")
    status = models.CharField(max_length = 50, verbose_name = "Status", blank=True)

class CommentData(models.Model):
    def __str__(self):
        return f"{self.subject}"
    class Meta:
        verbose_name_plural = "Comments"
    subject = models.CharField(max_length=50, verbose_name = "Subject")
    content = models.TextField(verbose_name = "Comment")
    data = models.ForeignKey(OverviewData, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.CharField(max_length = 50,verbose_name = "Created By", blank=True, null=True)
    topic = models.CharField(max_length = 50,verbose_name = "Topic", blank=True, null=True)

# #Policy
class PolicyData(models.Model):
    def __str__(self):
        return f"{self.subject}"
    class Meta:
        verbose_name_plural = "Segment Comments"
    subject = models.CharField(max_length=20, verbose_name = "Subject")
    content = models.TextField(verbose_name = "Comment")
    policy_nb = models.CharField(max_length=10, verbose_name = "Policy Number")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.CharField(max_length = 20,verbose_name = "Created By", blank=True, null=True)
    topic = models.CharField(max_length = 20,verbose_name = "Topic", blank=True, null=True)


