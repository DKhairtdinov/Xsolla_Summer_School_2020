import lib_main
from google.oauth2 import service_account

CREDENTIALS = service_account.Credentials.from_service_account_info()

DataFrame = lib_main.getFreshData(CREDENTIALS, 'findcsystem')

test_user = DataFrame[:]
test_user.reset_index(inplace=True, drop=True)

# получение dataframe'ов с данными скоринга
test_result = lib_main.workloadScoringByStatuses(test_user, 63, 7)
test_result_total = lib_main.workloadScoringTotal(test_result)
test_result_channel = lib_main.workloadScoringByStatusesByChannel(test_user, 63, 7)

#запись в таблицы
lib_main.insertScoreResultData(test_result, test_result_total, 'score_result_status', 'score_result_total',
                               'findcsystem', 'xsolla_summer_school')
lib_main.insertScoreChannelData(test_result_channel, 'findcsystem', 'xsolla_summer_school',
                                'score_result_status_channel')
