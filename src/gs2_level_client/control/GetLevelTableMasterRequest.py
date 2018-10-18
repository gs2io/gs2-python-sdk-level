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


class GetLevelTableMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "GetLevelTableMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetLevelTableMasterRequest, self).__init__(params)
        if params is None:
            self.__resource_pool_name = None
        else:
            self.set_resource_pool_name(params['resourcePoolName'] if 'resourcePoolName' in params.keys() else None)
        if params is None:
            self.__level_table_name = None
        else:
            self.set_level_table_name(params['levelTableName'] if 'levelTableName' in params.keys() else None)

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
        if resource_pool_name is not None and not (isinstance(resource_pool_name, str) or isinstance(resource_pool_name, unicode)):
            raise TypeError(type(resource_pool_name))
        self.__resource_pool_name = resource_pool_name

    def with_resource_pool_name(self, resource_pool_name):
        """
        リソースプールを設定
        :param resource_pool_name: リソースプール
        :type resource_pool_name: unicode
        :return: this
        :rtype: GetLevelTableMasterRequest
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
        if level_table_name is not None and not (isinstance(level_table_name, str) or isinstance(level_table_name, unicode)):
            raise TypeError(type(level_table_name))
        self.__level_table_name = level_table_name

    def with_level_table_name(self, level_table_name):
        """
        レベルテーブルを設定
        :param level_table_name: レベルテーブル
        :type level_table_name: unicode
        :return: this
        :rtype: GetLevelTableMasterRequest
        """
        self.set_level_table_name(level_table_name)
        return self
