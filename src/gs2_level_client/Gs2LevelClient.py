# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2LevelClient(AbstractGs2Client):

    ENDPOINT = "level"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2LevelClient, self).__init__(credential, region)

    def get_current_level_master(self, request):
        """
        レベルマスタを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetCurrentLevelMasterRequest.GetCurrentLevelMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetCurrentLevelMasterResult.GetCurrentLevelMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetCurrentLevelMasterRequest import GetCurrentLevelMasterRequest

        from gs2_level_client.control.GetCurrentLevelMasterResult import GetCurrentLevelMasterResult
        return GetCurrentLevelMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/status/master",
            service=self.ENDPOINT,
            component=GetCurrentLevelMasterRequest.Constant.MODULE,
            target_function=GetCurrentLevelMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_current_level_master(self, request):
        """
        レベルマスタを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.UpdateCurrentLevelMasterRequest.UpdateCurrentLevelMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.UpdateCurrentLevelMasterResult.UpdateCurrentLevelMasterResult
        """
        body = { 
            "settings": request.get_settings(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.UpdateCurrentLevelMasterRequest import UpdateCurrentLevelMasterRequest
        from gs2_level_client.control.UpdateCurrentLevelMasterResult import UpdateCurrentLevelMasterResult
        return UpdateCurrentLevelMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/status/master",
            service=self.ENDPOINT,
            component=UpdateCurrentLevelMasterRequest.Constant.MODULE,
            target_function=UpdateCurrentLevelMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_level_table_master(self, request):
        """
        レベルテーブルを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.CreateLevelTableMasterRequest.CreateLevelTableMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.CreateLevelTableMasterResult.CreateLevelTableMasterResult
        """
        body = { 
            "name": request.get_name(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.CreateLevelTableMasterRequest import CreateLevelTableMasterRequest
        from gs2_level_client.control.CreateLevelTableMasterResult import CreateLevelTableMasterResult
        return CreateLevelTableMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable",
            service=self.ENDPOINT,
            component=CreateLevelTableMasterRequest.Constant.MODULE,
            target_function=CreateLevelTableMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_level_table_master(self, request):
        """
        レベルテーブルを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.DeleteLevelTableMasterRequest.DeleteLevelTableMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DeleteLevelTableMasterRequest import DeleteLevelTableMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable/" + str(("null" if request.get_level_table_name() is None or request.get_level_table_name() == "" else url_encoder.encode(request.get_level_table_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteLevelTableMasterRequest.Constant.MODULE,
            target_function=DeleteLevelTableMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_level_table_master(self, request):
        """
        レベルテーブルの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.DescribeLevelTableMasterRequest.DescribeLevelTableMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.DescribeLevelTableMasterResult.DescribeLevelTableMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DescribeLevelTableMasterRequest import DescribeLevelTableMasterRequest

        from gs2_level_client.control.DescribeLevelTableMasterResult import DescribeLevelTableMasterResult
        return DescribeLevelTableMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable",
            service=self.ENDPOINT,
            component=DescribeLevelTableMasterRequest.Constant.MODULE,
            target_function=DescribeLevelTableMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_level_table_master(self, request):
        """
        レベルテーブルを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetLevelTableMasterRequest.GetLevelTableMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetLevelTableMasterResult.GetLevelTableMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetLevelTableMasterRequest import GetLevelTableMasterRequest

        from gs2_level_client.control.GetLevelTableMasterResult import GetLevelTableMasterResult
        return GetLevelTableMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable/" + str(("null" if request.get_level_table_name() is None or request.get_level_table_name() == "" else url_encoder.encode(request.get_level_table_name()))) + "",
            service=self.ENDPOINT,
            component=GetLevelTableMasterRequest.Constant.MODULE,
            target_function=GetLevelTableMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def create_level_threshold_master(self, request):
        """
        レベルアップ経験値閾値を新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.CreateLevelThresholdMasterRequest.CreateLevelThresholdMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.CreateLevelThresholdMasterResult.CreateLevelThresholdMasterResult
        """
        body = { 
            "threshold": request.get_threshold(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.CreateLevelThresholdMasterRequest import CreateLevelThresholdMasterRequest
        from gs2_level_client.control.CreateLevelThresholdMasterResult import CreateLevelThresholdMasterResult
        return CreateLevelThresholdMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable/" + str(("null" if request.get_level_table_name() is None or request.get_level_table_name() == "" else url_encoder.encode(request.get_level_table_name()))) + "/threshold",
            service=self.ENDPOINT,
            component=CreateLevelThresholdMasterRequest.Constant.MODULE,
            target_function=CreateLevelThresholdMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_level_threshold_master(self, request):
        """
        レベルアップ経験値閾値を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.DeleteLevelThresholdMasterRequest.DeleteLevelThresholdMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DeleteLevelThresholdMasterRequest import DeleteLevelThresholdMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable/" + str(("null" if request.get_level_table_name() is None or request.get_level_table_name() == "" else url_encoder.encode(request.get_level_table_name()))) + "/threshold/" + str(("null" if request.get_threshold() is None or request.get_threshold() == "" else url_encoder.encode(request.get_threshold()))) + "",
            service=self.ENDPOINT,
            component=DeleteLevelThresholdMasterRequest.Constant.MODULE,
            target_function=DeleteLevelThresholdMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_level_threshold_master(self, request):
        """
        レベルアップ経験値閾値の一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.DescribeLevelThresholdMasterRequest.DescribeLevelThresholdMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.DescribeLevelThresholdMasterResult.DescribeLevelThresholdMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DescribeLevelThresholdMasterRequest import DescribeLevelThresholdMasterRequest

        from gs2_level_client.control.DescribeLevelThresholdMasterResult import DescribeLevelThresholdMasterResult
        return DescribeLevelThresholdMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable/" + str(("null" if request.get_level_table_name() is None or request.get_level_table_name() == "" else url_encoder.encode(request.get_level_table_name()))) + "/threshold",
            service=self.ENDPOINT,
            component=DescribeLevelThresholdMasterRequest.Constant.MODULE,
            target_function=DescribeLevelThresholdMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_level_threshold_master(self, request):
        """
        レベルアップ経験値閾値を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetLevelThresholdMasterRequest.GetLevelThresholdMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetLevelThresholdMasterResult.GetLevelThresholdMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetLevelThresholdMasterRequest import GetLevelThresholdMasterRequest

        from gs2_level_client.control.GetLevelThresholdMasterResult import GetLevelThresholdMasterResult
        return GetLevelThresholdMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/levelTable/" + str(("null" if request.get_level_table_name() is None or request.get_level_table_name() == "" else url_encoder.encode(request.get_level_table_name()))) + "/threshold/" + str(("null" if request.get_threshold() is None or request.get_threshold() == "" else url_encoder.encode(request.get_threshold()))) + "",
            service=self.ENDPOINT,
            component=GetLevelThresholdMasterRequest.Constant.MODULE,
            target_function=GetLevelThresholdMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def export_master(self, request):
        """
        レベルマスターデータをエクスポートする<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.ExportMasterRequest.ExportMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.ExportMasterResult.ExportMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.ExportMasterRequest import ExportMasterRequest

        from gs2_level_client.control.ExportMasterResult import ExportMasterResult
        return ExportMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master",
            service=self.ENDPOINT,
            component=ExportMasterRequest.Constant.MODULE,
            target_function=ExportMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def create_resource_pool(self, request):
        """
        リソースプールを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.CreateResourcePoolRequest.CreateResourcePoolRequest
        :return: 結果
        :rtype: gs2_level_client.control.CreateResourcePoolResult.CreateResourcePoolResult
        """
        body = { 
            "name": request.get_name(),
            "serviceClass": request.get_service_class(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_level_cap_script() is not None:
            body["levelCapScript"] = request.get_level_cap_script()
        if request.get_change_experience_trigger_script() is not None:
            body["changeExperienceTriggerScript"] = request.get_change_experience_trigger_script()
        if request.get_change_experience_done_trigger_script() is not None:
            body["changeExperienceDoneTriggerScript"] = request.get_change_experience_done_trigger_script()
        if request.get_change_level_trigger_script() is not None:
            body["changeLevelTriggerScript"] = request.get_change_level_trigger_script()
        if request.get_change_level_done_trigger_script() is not None:
            body["changeLevelDoneTriggerScript"] = request.get_change_level_done_trigger_script()
        if request.get_change_level_cap_trigger_script() is not None:
            body["changeLevelCapTriggerScript"] = request.get_change_level_cap_trigger_script()
        if request.get_change_level_cap_done_trigger_script() is not None:
            body["changeLevelCapDoneTriggerScript"] = request.get_change_level_cap_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.CreateResourcePoolRequest import CreateResourcePoolRequest
        from gs2_level_client.control.CreateResourcePoolResult import CreateResourcePoolResult
        return CreateResourcePoolResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool",
            service=self.ENDPOINT,
            component=CreateResourcePoolRequest.Constant.MODULE,
            target_function=CreateResourcePoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_resource_pool(self, request):
        """
        リソースプールを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.DeleteResourcePoolRequest.DeleteResourcePoolRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DeleteResourcePoolRequest import DeleteResourcePoolRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteResourcePoolRequest.Constant.MODULE,
            target_function=DeleteResourcePoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_resource_pool(self, request):
        """
        リソースプールの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.DescribeResourcePoolRequest.DescribeResourcePoolRequest
        :return: 結果
        :rtype: gs2_level_client.control.DescribeResourcePoolResult.DescribeResourcePoolResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DescribeResourcePoolRequest import DescribeResourcePoolRequest

        from gs2_level_client.control.DescribeResourcePoolResult import DescribeResourcePoolResult
        return DescribeResourcePoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool",
            service=self.ENDPOINT,
            component=DescribeResourcePoolRequest.Constant.MODULE,
            target_function=DescribeResourcePoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_resource_pool(self, request):
        """
        リソースプールを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetResourcePoolRequest.GetResourcePoolRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetResourcePoolResult.GetResourcePoolResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetResourcePoolRequest import GetResourcePoolRequest

        from gs2_level_client.control.GetResourcePoolResult import GetResourcePoolResult
        return GetResourcePoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "",
            service=self.ENDPOINT,
            component=GetResourcePoolRequest.Constant.MODULE,
            target_function=GetResourcePoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_resource_pool_status(self, request):
        """
        リソースプールの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetResourcePoolStatusRequest.GetResourcePoolStatusRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetResourcePoolStatusResult.GetResourcePoolStatusResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetResourcePoolStatusRequest import GetResourcePoolStatusRequest

        from gs2_level_client.control.GetResourcePoolStatusResult import GetResourcePoolStatusResult
        return GetResourcePoolStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/status",
            service=self.ENDPOINT,
            component=GetResourcePoolStatusRequest.Constant.MODULE,
            target_function=GetResourcePoolStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_resource_pool(self, request):
        """
        リソースプールを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.UpdateResourcePoolRequest.UpdateResourcePoolRequest
        :return: 結果
        :rtype: gs2_level_client.control.UpdateResourcePoolResult.UpdateResourcePoolResult
        """
        body = { 
            "serviceClass": request.get_service_class(),
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_level_cap_script() is not None:
            body["levelCapScript"] = request.get_level_cap_script()
        if request.get_change_experience_trigger_script() is not None:
            body["changeExperienceTriggerScript"] = request.get_change_experience_trigger_script()
        if request.get_change_experience_done_trigger_script() is not None:
            body["changeExperienceDoneTriggerScript"] = request.get_change_experience_done_trigger_script()
        if request.get_change_level_trigger_script() is not None:
            body["changeLevelTriggerScript"] = request.get_change_level_trigger_script()
        if request.get_change_level_done_trigger_script() is not None:
            body["changeLevelDoneTriggerScript"] = request.get_change_level_done_trigger_script()
        if request.get_change_level_cap_trigger_script() is not None:
            body["changeLevelCapTriggerScript"] = request.get_change_level_cap_trigger_script()
        if request.get_change_level_cap_done_trigger_script() is not None:
            body["changeLevelCapDoneTriggerScript"] = request.get_change_level_cap_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.UpdateResourcePoolRequest import UpdateResourcePoolRequest
        from gs2_level_client.control.UpdateResourcePoolResult import UpdateResourcePoolResult
        return UpdateResourcePoolResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateResourcePoolRequest.Constant.MODULE,
            target_function=UpdateResourcePoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_resource_type_master(self, request):
        """
        リソースタイプを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.CreateResourceTypeMasterRequest.CreateResourceTypeMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.CreateResourceTypeMasterResult.CreateResourceTypeMasterResult
        """
        body = { 
            "name": request.get_name(),
            "levelTableName": request.get_level_table_name(),
            "defaultLevelCap": request.get_default_level_cap(),
            "maxLevelCap": request.get_max_level_cap(),
        }

        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        if request.get_default_experience() is not None:
            body["defaultExperience"] = request.get_default_experience()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.CreateResourceTypeMasterRequest import CreateResourceTypeMasterRequest
        from gs2_level_client.control.CreateResourceTypeMasterResult import CreateResourceTypeMasterResult
        return CreateResourceTypeMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/resourceType",
            service=self.ENDPOINT,
            component=CreateResourceTypeMasterRequest.Constant.MODULE,
            target_function=CreateResourceTypeMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_resource_type_master(self, request):
        """
        リソースタイプを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.DeleteResourceTypeMasterRequest.DeleteResourceTypeMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DeleteResourceTypeMasterRequest import DeleteResourceTypeMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteResourceTypeMasterRequest.Constant.MODULE,
            target_function=DeleteResourceTypeMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_resource_type_master(self, request):
        """
        リソースタイプの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.DescribeResourceTypeMasterRequest.DescribeResourceTypeMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.DescribeResourceTypeMasterResult.DescribeResourceTypeMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DescribeResourceTypeMasterRequest import DescribeResourceTypeMasterRequest

        from gs2_level_client.control.DescribeResourceTypeMasterResult import DescribeResourceTypeMasterResult
        return DescribeResourceTypeMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/resourceType",
            service=self.ENDPOINT,
            component=DescribeResourceTypeMasterRequest.Constant.MODULE,
            target_function=DescribeResourceTypeMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_resource_type_master(self, request):
        """
        リソースタイプを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetResourceTypeMasterRequest.GetResourceTypeMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetResourceTypeMasterResult.GetResourceTypeMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetResourceTypeMasterRequest import GetResourceTypeMasterRequest

        from gs2_level_client.control.GetResourceTypeMasterResult import GetResourceTypeMasterResult
        return GetResourceTypeMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "",
            service=self.ENDPOINT,
            component=GetResourceTypeMasterRequest.Constant.MODULE,
            target_function=GetResourceTypeMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_resource_type_master(self, request):
        """
        リソースタイプを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.UpdateResourceTypeMasterRequest.UpdateResourceTypeMasterRequest
        :return: 結果
        :rtype: gs2_level_client.control.UpdateResourceTypeMasterResult.UpdateResourceTypeMasterResult
        """
        body = { 
            "levelTableName": request.get_level_table_name(),
            "defaultLevelCap": request.get_default_level_cap(),
            "maxLevelCap": request.get_max_level_cap(),
        }
        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        if request.get_default_experience() is not None:
            body["defaultExperience"] = request.get_default_experience()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.UpdateResourceTypeMasterRequest import UpdateResourceTypeMasterRequest
        from gs2_level_client.control.UpdateResourceTypeMasterResult import UpdateResourceTypeMasterResult
        return UpdateResourceTypeMasterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/master/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateResourceTypeMasterRequest.Constant.MODULE,
            target_function=UpdateResourceTypeMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def change_level_cap_by_stamp_sheet(self, request):
        """
        スタンプシートを使用してレベルキャップを変更します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.ChangeLevelCapByStampSheetRequest.ChangeLevelCapByStampSheetRequest
        :return: 結果
        :rtype: gs2_level_client.control.ChangeLevelCapByStampSheetResult.ChangeLevelCapByStampSheetResult
        """
        body = { 
            "sheet": request.get_sheet(),
            "keyName": request.get_key_name(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.ChangeLevelCapByStampSheetRequest import ChangeLevelCapByStampSheetRequest
        from gs2_level_client.control.ChangeLevelCapByStampSheetResult import ChangeLevelCapByStampSheetResult
        return ChangeLevelCapByStampSheetResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/status/levelCap",
            service=self.ENDPOINT,
            component=ChangeLevelCapByStampSheetRequest.Constant.MODULE,
            target_function=ChangeLevelCapByStampSheetRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def change_level_cap_by_user_id(self, request):
        """
        レベルキャップを変更します<br>
        <br>
        消費クォーター: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.ChangeLevelCapByUserIdRequest.ChangeLevelCapByUserIdRequest
        :return: 結果
        :rtype: gs2_level_client.control.ChangeLevelCapByUserIdResult.ChangeLevelCapByUserIdResult
        """
        body = { 
            "levelCap": request.get_level_cap(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.ChangeLevelCapByUserIdRequest import ChangeLevelCapByUserIdRequest
        from gs2_level_client.control.ChangeLevelCapByUserIdResult import ChangeLevelCapByUserIdResult
        return ChangeLevelCapByUserIdResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/" + str(("null" if request.get_status_id() is None or request.get_status_id() == "" else url_encoder.encode(request.get_status_id()))) + "/levelCap",
            service=self.ENDPOINT,
            component=ChangeLevelCapByUserIdRequest.Constant.MODULE,
            target_function=ChangeLevelCapByUserIdRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def change_level_cap_by_user_id_and_resource_type(self, request):
        """
        レベルキャップを変更します<br>
        <br>
        消費クォーター: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.ChangeLevelCapByUserIdAndResourceTypeRequest.ChangeLevelCapByUserIdAndResourceTypeRequest
        :return: 結果
        :rtype: gs2_level_client.control.ChangeLevelCapByUserIdAndResourceTypeResult.ChangeLevelCapByUserIdAndResourceTypeResult
        """
        body = { 
            "levelCap": request.get_level_cap(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.ChangeLevelCapByUserIdAndResourceTypeRequest import ChangeLevelCapByUserIdAndResourceTypeRequest
        from gs2_level_client.control.ChangeLevelCapByUserIdAndResourceTypeResult import ChangeLevelCapByUserIdAndResourceTypeResult
        return ChangeLevelCapByUserIdAndResourceTypeResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "/levelCap",
            service=self.ENDPOINT,
            component=ChangeLevelCapByUserIdAndResourceTypeRequest.Constant.MODULE,
            target_function=ChangeLevelCapByUserIdAndResourceTypeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def describe_status(self, request):
        """
        ステータス一覧を取得します<br>
        <br>
        本APIは statusIds に取得するリソースIDのリストを指定出来ます。<br>
        リソースIDリストを指定しない場合は全てのリソースのステータスを応答しますが、IDを指定する場合と比較して2倍のクォーターを消費します。<br>
        ステータスを取得する段階でリソースIDが明らかな場合はリソースIDのリストを指定することをお勧めします。<br>
        <br>
        消費クォーター: 取得件数 × 3(リソースIDを省略した場合は2倍)<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.DescribeStatusRequest.DescribeStatusRequest
        :return: 結果
        :rtype: gs2_level_client.control.DescribeStatusResult.DescribeStatusResult
        """
        query_strings = {
            'statusIds': request.get_status_ids(),
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DescribeStatusRequest import DescribeStatusRequest

        from gs2_level_client.control.DescribeStatusResult import DescribeStatusResult
        return DescribeStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/my/status",
            service=self.ENDPOINT,
            component=DescribeStatusRequest.Constant.MODULE,
            target_function=DescribeStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_status_by_user_id(self, request):
        """
        ステータスを一覧を取得します<br>
        <br>
        本APIは statusIds に取得するリソースIDのリストを指定出来ます。<br>
        リソースIDリストを指定しない場合は全てのリソースのステータスを応答しますが、IDを指定する場合と比較して2倍のクォーターを消費します。<br>
        ステータスを取得する段階でリソースIDが明らかな場合はリソースIDのリストを指定することをお勧めします。<br>
        <br>
        消費クォーター: 取得件数 × 3(リソースIDを省略した場合は2倍)<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.DescribeStatusByUserIdRequest.DescribeStatusByUserIdRequest
        :return: 結果
        :rtype: gs2_level_client.control.DescribeStatusByUserIdResult.DescribeStatusByUserIdResult
        """
        query_strings = {
            'statusIds': request.get_status_ids(),
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.DescribeStatusByUserIdRequest import DescribeStatusByUserIdRequest

        from gs2_level_client.control.DescribeStatusByUserIdResult import DescribeStatusByUserIdResult
        return DescribeStatusByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status",
            service=self.ENDPOINT,
            component=DescribeStatusByUserIdRequest.Constant.MODULE,
            target_function=DescribeStatusByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_status(self, request):
        """
        ステータスを取得します<br>
        <br>
        消費クォーター: 3<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetStatusRequest.GetStatusRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetStatusResult.GetStatusResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetStatusRequest import GetStatusRequest

        from gs2_level_client.control.GetStatusResult import GetStatusResult
        return GetStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/my/status/" + str(("null" if request.get_status_id() is None or request.get_status_id() == "" else url_encoder.encode(request.get_status_id()))) + "",
            service=self.ENDPOINT,
            component=GetStatusRequest.Constant.MODULE,
            target_function=GetStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_status_by_resource_type(self, request):
        """
        ステータスを取得します<br>
        <br>
        消費クォーター: 3<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetStatusByResourceTypeRequest.GetStatusByResourceTypeRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetStatusByResourceTypeResult.GetStatusByResourceTypeResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetStatusByResourceTypeRequest import GetStatusByResourceTypeRequest

        from gs2_level_client.control.GetStatusByResourceTypeResult import GetStatusByResourceTypeResult
        return GetStatusByResourceTypeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/my/status/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "",
            service=self.ENDPOINT,
            component=GetStatusByResourceTypeRequest.Constant.MODULE,
            target_function=GetStatusByResourceTypeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_status_by_user_id(self, request):
        """
        ステータスを取得します<br>
        <br>
        消費クォーター: 3<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetStatusByUserIdRequest.GetStatusByUserIdRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetStatusByUserIdResult.GetStatusByUserIdResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetStatusByUserIdRequest import GetStatusByUserIdRequest

        from gs2_level_client.control.GetStatusByUserIdResult import GetStatusByUserIdResult
        return GetStatusByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/" + str(("null" if request.get_status_id() is None or request.get_status_id() == "" else url_encoder.encode(request.get_status_id()))) + "",
            service=self.ENDPOINT,
            component=GetStatusByUserIdRequest.Constant.MODULE,
            target_function=GetStatusByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_status_by_user_id_and_resource_type(self, request):
        """
        ステータスを取得します<br>
        <br>
        消費クォーター: 3<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_level_client.control.GetStatusByUserIdAndResourceTypeRequest.GetStatusByUserIdAndResourceTypeRequest
        :return: 結果
        :rtype: gs2_level_client.control.GetStatusByUserIdAndResourceTypeResult.GetStatusByUserIdAndResourceTypeResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.GetStatusByUserIdAndResourceTypeRequest import GetStatusByUserIdAndResourceTypeRequest

        from gs2_level_client.control.GetStatusByUserIdAndResourceTypeResult import GetStatusByUserIdAndResourceTypeResult
        return GetStatusByUserIdAndResourceTypeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "",
            service=self.ENDPOINT,
            component=GetStatusByUserIdAndResourceTypeRequest.Constant.MODULE,
            target_function=GetStatusByUserIdAndResourceTypeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def increase_experience_by_stamp_sheet(self, request):
        """
        スタンプシートを使用して経験値を加算します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.IncreaseExperienceByStampSheetRequest.IncreaseExperienceByStampSheetRequest
        :return: 結果
        :rtype: gs2_level_client.control.IncreaseExperienceByStampSheetResult.IncreaseExperienceByStampSheetResult
        """
        body = { 
            "sheet": request.get_sheet(),
            "keyName": request.get_key_name(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.IncreaseExperienceByStampSheetRequest import IncreaseExperienceByStampSheetRequest
        from gs2_level_client.control.IncreaseExperienceByStampSheetResult import IncreaseExperienceByStampSheetResult
        return IncreaseExperienceByStampSheetResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/status",
            service=self.ENDPOINT,
            component=IncreaseExperienceByStampSheetRequest.Constant.MODULE,
            target_function=IncreaseExperienceByStampSheetRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def increase_experience_by_user_id(self, request):
        """
        経験値を加算します<br>
        <br>
        消費クォーター: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.IncreaseExperienceByUserIdRequest.IncreaseExperienceByUserIdRequest
        :return: 結果
        :rtype: gs2_level_client.control.IncreaseExperienceByUserIdResult.IncreaseExperienceByUserIdResult
        """
        body = { 
            "value": request.get_value(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.IncreaseExperienceByUserIdRequest import IncreaseExperienceByUserIdRequest
        from gs2_level_client.control.IncreaseExperienceByUserIdResult import IncreaseExperienceByUserIdResult
        return IncreaseExperienceByUserIdResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/" + str(("null" if request.get_status_id() is None or request.get_status_id() == "" else url_encoder.encode(request.get_status_id()))) + "",
            service=self.ENDPOINT,
            component=IncreaseExperienceByUserIdRequest.Constant.MODULE,
            target_function=IncreaseExperienceByUserIdRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def increase_experience_by_user_id_and_resource_type(self, request):
        """
        経験値を加算します<br>
        <br>
        消費クォーター: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.IncreaseExperienceByUserIdAndResourceTypeRequest.IncreaseExperienceByUserIdAndResourceTypeRequest
        :return: 結果
        :rtype: gs2_level_client.control.IncreaseExperienceByUserIdAndResourceTypeResult.IncreaseExperienceByUserIdAndResourceTypeResult
        """
        body = { 
            "value": request.get_value(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.IncreaseExperienceByUserIdAndResourceTypeRequest import IncreaseExperienceByUserIdAndResourceTypeRequest
        from gs2_level_client.control.IncreaseExperienceByUserIdAndResourceTypeResult import IncreaseExperienceByUserIdAndResourceTypeResult
        return IncreaseExperienceByUserIdAndResourceTypeResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "",
            service=self.ENDPOINT,
            component=IncreaseExperienceByUserIdAndResourceTypeRequest.Constant.MODULE,
            target_function=IncreaseExperienceByUserIdAndResourceTypeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def set_experience_by_user_id(self, request):
        """
        経験値を設定します<br>
        <br>
        消費クォーター: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.SetExperienceByUserIdRequest.SetExperienceByUserIdRequest
        :return: 結果
        :rtype: gs2_level_client.control.SetExperienceByUserIdResult.SetExperienceByUserIdResult
        """
        body = { 
            "experience": request.get_experience(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.SetExperienceByUserIdRequest import SetExperienceByUserIdRequest
        from gs2_level_client.control.SetExperienceByUserIdResult import SetExperienceByUserIdResult
        return SetExperienceByUserIdResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/" + str(("null" if request.get_status_id() is None or request.get_status_id() == "" else url_encoder.encode(request.get_status_id()))) + "",
            service=self.ENDPOINT,
            component=SetExperienceByUserIdRequest.Constant.MODULE,
            target_function=SetExperienceByUserIdRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def set_experience_by_user_id_and_resource_type(self, request):
        """
        経験値を設定します<br>
        <br>
        消費クォーター: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_level_client.control.SetExperienceByUserIdAndResourceTypeRequest.SetExperienceByUserIdAndResourceTypeRequest
        :return: 結果
        :rtype: gs2_level_client.control.SetExperienceByUserIdAndResourceTypeResult.SetExperienceByUserIdAndResourceTypeResult
        """
        body = { 
            "experience": request.get_experience(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_level_client.control.SetExperienceByUserIdAndResourceTypeRequest import SetExperienceByUserIdAndResourceTypeRequest
        from gs2_level_client.control.SetExperienceByUserIdAndResourceTypeResult import SetExperienceByUserIdAndResourceTypeResult
        return SetExperienceByUserIdAndResourceTypeResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/resourcePool/" + str(("null" if request.get_resource_pool_name() is None or request.get_resource_pool_name() == "" else url_encoder.encode(request.get_resource_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/status/resourceType/" + str(("null" if request.get_resource_type_name() is None or request.get_resource_type_name() == "" else url_encoder.encode(request.get_resource_type_name()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "",
            service=self.ENDPOINT,
            component=SetExperienceByUserIdAndResourceTypeRequest.Constant.MODULE,
            target_function=SetExperienceByUserIdAndResourceTypeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))
