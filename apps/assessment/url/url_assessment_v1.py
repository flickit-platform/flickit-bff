from django.urls import path

from assessment.views import (projectviews, reportviews, confidence_levels_views, assessment_views, dashboard_views,
                              advice_views, assessment_user_roles_views, maturity_level_views, questionnaire_views,
                              question_views, assessment_insight_views, assessment_analysis_views, assessment_report_views)

urlpatterns = [
    path("", projectviews.AssessmentProjectApi.as_view()),
    path("<uuid:assessment_id>/calculate/", maturity_level_views.MaturityLevelCalculateApi.as_view()),
    path("<uuid:assessment_id>/questions/<int:question_id>/answer-history/",
         question_views.AnswerHistoryApi.as_view()),
    path("<uuid:assessment_id>/questionnaires/<int:questionnaire_id>/",
         questionnaire_views.LoadQuestionsWithQuestionnairesApi.as_view()),
    path("<uuid:assessment_id>/subjects/<int:subject_id>/progress/", reportviews.SubjectProgressApi.as_view()),
    path("<uuid:assessment_id>/subjects/<int:subject_id>/init-insight/", assessment_insight_views.SubjectInitInsightApi.as_view()),
    path("<uuid:assessment_id>/report/attributes/<int:attribute_id>/",
         reportviews.AssessmentAttributesReportApi.as_view()),
    path("<uuid:assessment_id>/report/attributes/<int:attribute_id>/stats/",
         reportviews.AttributeScoreStatsAPIView.as_view()),
    path("<uuid:assessment_id>/", projectviews.AssessmentApi.as_view()),
    path("<uuid:assessment_id>/users/",
         assessment_user_roles_views.UsersAccessToAssessmentApi.as_view()),
    path("<uuid:assessment_id>/assessment-user-roles/",
         assessment_user_roles_views.UsersRolesInAssessmentApi.as_view()),
    path("<uuid:assessment_id>/assessment-user-roles/<uuid:user_id>/",
         assessment_user_roles_views.UserRolesInAssessmentApi.as_view()),
    path("<uuid:assessment_id>/calculate-confidence/", confidence_levels_views.CalculateConfidenceApi.as_view()),
    path("<uuid:assessment_id>/advice/", advice_views.AdviceView.as_view()),
    path("<uuid:assessment_id>/pre-advice-info/", assessment_views.PreAdviceInfoApi.as_view()),
    path("<uuid:assessment_id>/approve-answer/", assessment_views.ApproveAnswerApi.as_view()),
    path("<uuid:assessment_id>/advice-narration/", advice_views.AdviceNarrationView.as_view()),
    path("<uuid:assessment_id>/advice-narration-ai/", advice_views.AdviceNarrationAiView.as_view()),
    path("<uuid:assessment_id>/invite/", assessment_views.InviteUsersAssessmentsApi.as_view()),
    path("<uuid:assessment_id>/invitees/", assessment_views.InviteesAssessmentsApi.as_view()),
    path("<uuid:assessment_id>/graphical-report/", assessment_report_views.GraphicalReportApi.as_view()),
    path("<uuid:assessment_id>/report-publish-status/", assessment_report_views.ReportPublishStatus.as_view()),
    path("<uuid:assessment_id>/insight/", assessment_insight_views.AssessmentInsightApi.as_view()),
    path("<uuid:assessment_id>/overall-insight/", assessment_insight_views.AssessmentInsightApi.as_view()),
    path("<uuid:assessment_id>/init-overall-insight/", assessment_insight_views.InitAssessmentInsightApi.as_view()),
    path("<uuid:assessment_id>/subjects/<int:subject_id>/insight/",
         assessment_insight_views.AssessmentSubjectLoadInsightApi.as_view()),
    path("<uuid:assessment_id>/subjects/<int:subject_id>/approve-insight/",
         assessment_insight_views.ApproveSubjectInsightApi.as_view()),
    path("<uuid:assessment_id>/attributes/<int:attribute_id>/approve-insight/",
         assessment_insight_views.ApproveAttributeInsightApi.as_view()),
    path("<uuid:assessment_id>/attributes/<int:attribute_id>/insight/",
         assessment_insight_views.AssessmentAttributeInsightApi.as_view()),
    path("<uuid:assessment_id>/attributes/<int:attribute_id>/ai-insight/",
         assessment_insight_views.AssessmentAttributeAiInsightApi.as_view()),
    path("<uuid:assessment_id>/approve-insights/",
         assessment_insight_views.ApproveAllAssessmentInsightsApi.as_view()),
    path("<uuid:assessment_id>/analysis-input/", assessment_analysis_views.UploadAnalysisFileApi.as_view()),
    path("<uuid:assessment_id>/migrate-kit-version/", assessment_views.AssessmentMigrateKitVersionApi.as_view()),
    path("<uuid:assessment_id>/assign-kit-custom/", assessment_views.AssessmentAssignCustomKitApi.as_view()),
    path("<uuid:assessment_id>/dashboard/", dashboard_views.AssessmentDashboardApi.as_view()),
    path("<uuid:assessment_id>/permissions/", assessment_views.AssessmentPermissionsListApi.as_view()),
    path("<uuid:assessment_id>/approve-overall-insight/", assessment_insight_views.ApproveAssessmentInsightApi.as_view()),
    path("<uuid:assessment_id>/grant-report-access/", assessment_views.GrantReportAccessApi.as_view()),
    path("<uuid:assessment_id>/users-with-report-access/", assessment_views.UsersWithReportAccessApi.as_view()),
    path("<uuid:assessment_id>/report-metadata/", assessment_views.ReportMetadataAPI.as_view()),
    path("<uuid:assessment_id>/questions/<int:question_id>/issues/", assessment_views.QuestionIssuesApi.as_view()),
]
