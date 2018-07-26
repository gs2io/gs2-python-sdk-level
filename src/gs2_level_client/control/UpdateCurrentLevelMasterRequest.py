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


class UpdateCurrentLevelMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "UpdateCurrentLevelMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateCurrentLevelMasterRequest, self).__init__(params)
        if params is None:
            self.__resource_pool_name = None
        else:
            self.set_resource_pool_name(params['resourcePoolName'] if 'resourcePoolName' in params.keys() else None)
        if params is None:
            self.__settings = None
        else:
            self.set_settings(params['settings'] if 'settings' in params.keys() else None)

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
        :rtype: UpdateCurrentLevelMasterRequest
        """
        self.set_resource_pool_name(resource_pool_name)
        return self

    def get_settings(self):
        """
        レベルマスターデータを取得
        :return: レベルマスターデータ
        :rtype: unicode
        """
        return self.__settings

    def set_settings(self, settings):
        """
        レベルマスターデータを設定
        :param settings: レベルマスターデータ
        :type settings: unicode
        """
        if settings and not (isinstance(settings, str) or isinstance(settings, unicode)):
            raise TypeError(type(settings))
        self.__settings = settings

    def with_settings(self, settings):
        """
        レベルマスターデータを設定
        :param settings: レベルマスターデータ
        :type settings: unicode
        :return: this
        :rtype: UpdateCurrentLevelMasterRequest
        """
        self.set_settings(settings)
        return self
