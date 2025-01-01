from django.urls import path

from assessment.views import (projectviews, reportviews, confidence_levels_views, assessment_views, dashboard_views,
                              advice_views, assessment_user_roles_views, maturity_level_views, questionnaire_views,
                              question_views, assessment_insight_views, assessment_analysis_views)

urlpatterns = [
    path("", projectviews.AssessmentProjectApi.as_view()),
    path("<uuid:assessment_id>/calculate/", maturity_level_views.MaturityLevelCalculateApi.as_view()),
    path("<uuid:assessment_id>/questions/<int:question_id>/answer-history/",
         question_views.AnswerHistoryApi.as_view()),
    path("<uuid:assessment_id>/questionnaires/<int:questionnaire_id>/",
         questionnaire_views.LoadQuestionsWithQuestionnairesApi.as_view()),
    path("<uuid:assessment_id>/subjects/<int:subject_id>/progress/", reportviews.SubjectProgressApi.as_view()),
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
    path("<uuid:assessment_id>/advice-narration/", advice_views.AdviceNarrationView.as_view()),
    path("<uuid:assessment_id>/advice-narration-ai/", advice_views.AdviceNarrationAiView.as_view()),
    path("<uuid:assessment_id>/ai-report/attributes/<int:attribute_id>/",
         reportviews.AssessmentAttributesReportAiApi.as_view()),
    path("<uuid:assessment_id>/invite/", assessment_views.InviteUsersAssessmentsApi.as_view()),
    path("<uuid:assessment_id>/invitees/", assessment_views.InviteesAssessmentsApi.as_view()),
    path("<uuid:assessment_id>/insight/", assessment_insight_views.AssessmentInsightApi.as_view()),
    path("<uuid:assessment_id>/insight/subjects/<int:subject_id>/",
         assessment_insight_views.AssessmentSubjectInsightApi.as_view()),
    path("<uuid:assessment_id>/attributes/<int:attribute_id>/approve-insight/",
         assessment_insight_views.ApproveAttributeInsightApi.as_view()),
    path("<uuid:assessment_id>/analysis-input/", assessment_analysis_views.UploadAnalysisFileApi.as_view()),
    path("<uuid:assessment_id>/migrate-kit-version/", assessment_views.AssessmentMigrateKitVersionApi.as_view()),
    path("<uuid:assessment_id>/assign-kit-custom/", assessment_views.AssessmentAssignCustomKitApi.as_view()),
    path("<uuid:assessment_id>/dashboard/", dashboard_views.AssessmentDashboardApi.as_view()),
    path("<uuid:assessment_id>/permissions/", assessment_views.AssessmentPermissionsListApi.as_view()),
]
