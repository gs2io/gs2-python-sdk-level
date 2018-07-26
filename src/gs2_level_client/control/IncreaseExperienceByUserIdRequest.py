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


class IncreaseExperienceByUserIdRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "IncreaseExperienceByUserId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(IncreaseExperienceByUserIdRequest, self).__init__(params)
        if params is None:
            self.__resource_pool_name = None
        else:
            self.set_resource_pool_name(params['resourcePoolName'] if 'resourcePoolName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__status_id = None
        else:
            self.set_status_id(params['statusId'] if 'statusId' in params.keys() else None)
        if params is None:
            self.__value = None
        else:
            self.set_value(params['value'] if 'value' in params.keys() else None)

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
        :rtype: IncreaseExperienceByUserIdRequest
        """
        self.set_resource_pool_name(resource_pool_name)
        return self

    def get_user_id(self):
        """
        ステータスを取得
        :return: ステータス
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ステータスを設定
        :param user_id: ステータス
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ステータスを設定
        :param user_id: ステータス
        :type user_id: unicode
        :return: this
        :rtype: IncreaseExperienceByUserIdRequest
        """
        self.set_user_id(user_id)
        return self

    def get_status_id(self):
        """
        ステータスIDを取得
        :return: ステータスID
        :rtype: unicode
        """
        return self.__status_id

    def set_status_id(self, status_id):
        """
        ステータスIDを設定
        :param status_id: ステータスID
        :type status_id: unicode
        """
        if status_id and not (isinstance(status_id, str) or isinstance(status_id, unicode)):
            raise TypeError(type(status_id))
        self.__status_id = status_id

    def with_status_id(self, status_id):
        """
        ステータスIDを設定
        :param status_id: ステータスID
        :type status_id: unicode
        :return: this
        :rtype: IncreaseExperienceByUserIdRequest
        """
        self.set_status_id(status_id)
        return self

    def get_value(self):
        """
        経験値の加算量を取得
        :return: 経験値の加算量
        :rtype: long
        """
        return self.__value

    def set_value(self, value):
        """
        経験値の加算量を設定
        :param value: 経験値の加算量
        :type value: long
        """
        if value and not (isinstance(value, int) or isinstance(value, long)):
            raise TypeError(type(value))
        self.__value = value

    def with_value(self, value):
        """
        経験値の加算量を設定
        :param value: 経験値の加算量
        :type value: long
        :return: this
        :rtype: IncreaseExperienceByUserIdRequest
        """
        self.set_value(value)
        return self
