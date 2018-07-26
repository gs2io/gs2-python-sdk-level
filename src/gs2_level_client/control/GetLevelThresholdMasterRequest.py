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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_level_client.Gs2Level import Gs2Level


class GetLevelThresholdMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "GetLevelThresholdMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetLevelThresholdMasterRequest, self).__init__(params)
        if params is None:
            self.__resource_pool_name = None
        else:
            self.set_resource_pool_name(params['resourcePoolName'] if 'resourcePoolName' in params.keys() else None)
        if params is None:
            self.__level_table_name = None
        else:
            self.set_level_table_name(params['levelTableName'] if 'levelTableName' in params.keys() else None)
        if params is None:
            self.__threshold = None
        else:
            self.set_threshold(params['threshold'] if 'threshold' in params.keys() else None)

    def get_resource_pool_name(self):
        """
        リソースプールを取得
        :return: リソースプール
        :rtype: unicode
        """
        return self.__resource_pool_name

    def set_resource_pool_name(self, resource_pool_name):
        """
        リソースプールを設定
        :param resource_pool_name: リソースプール
        :type resource_pool_name: unicode
        """
        if resource_pool_name and not (isinstance(resource_pool_name, str) or isinstance(resource_pool_name, unicode)):
            raise TypeError(type(resource_pool_name))
        self.__resource_pool_name = resource_pool_name

    def with_resource_pool_name(self, resource_pool_name):
        """
        リソースプールを設定
        :param resource_pool_name: リソースプール
        :type resource_pool_name: unicode
        :return: this
        :rtype: GetLevelThresholdMasterRequest
        """
        self.set_resource_pool_name(resource_pool_name)
        return self

    def get_level_table_name(self):
        """
        レベルテーブルを取得
        :return: レベルテーブル
        :rtype: unicode
        """
        return self.__level_table_name

    def set_level_table_name(self, level_table_name):
        """
        レベルテーブルを設定
        :param level_table_name: レベルテーブル
        :type level_table_name: unicode
        """
        if level_table_name and not (isinstance(level_table_name, str) or isinstance(level_table_name, unicode)):
            raise TypeError(type(level_table_name))
        self.__level_table_name = level_table_name

    def with_level_table_name(self, level_table_name):
        """
        レベルテーブルを設定
        :param level_table_name: レベルテーブル
        :type level_table_name: unicode
        :return: this
        :rtype: GetLevelThresholdMasterRequest
        """
        self.set_level_table_name(level_table_name)
        return self

    def get_threshold(self):
        """
        レベルアップ経験値閾値を取得
        :return: レベルアップ経験値閾値
        :rtype: long
        """
        return self.__threshold

    def set_threshold(self, threshold):
        """
        レベルアップ経験値閾値を設定
        :param threshold: レベルアップ経験値閾値
        :type threshold: long
        """
        if threshold and not (isinstance(threshold, int) or isinstance(threshold, long)):
            raise TypeError(type(threshold))
        self.__threshold = threshold

    def with_threshold(self, threshold):
        """
        レベルアップ経験値閾値を設定
        :param threshold: レベルアップ経験値閾値
        :type threshold: long
        :return: this
        :rtype: GetLevelThresholdMasterRequest
        """
        self.set_threshold(threshold)
        return self
