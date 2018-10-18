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


class IncreaseExperienceByUserIdAndResourceTypeRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "IncreaseExperienceByUserId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(IncreaseExperienceByUserIdAndResourceTypeRequest, self).__init__(params)
        if params is None:
            self.__resource_pool_name = None
        else:
            self.set_resource_pool_name(params['resourcePoolName'] if 'resourcePoolName' in params.keys() else None)
        if params is None:
            self.__resource_type_name = None
        else:
            self.set_resource_type_name(params['resourceTypeName'] if 'resourceTypeName' in params.keys() else None)
        if params is None:
            self.__resource_id = None
        else:
            self.set_resource_id(params['resourceId'] if 'resourceId' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
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
        if resource_pool_name is not None and not (isinstance(resource_pool_name, str) or isinstance(resource_pool_name, unicode)):
            raise TypeError(type(resource_pool_name))
        self.__resource_pool_name = resource_pool_name

    def with_resource_pool_name(self, resource_pool_name):
        """
        リソースプールを設定
        :param resource_pool_name: リソースプール
        :type resource_pool_name: unicode
        :return: this
        :rtype: IncreaseExperienceByUserIdAndResourceTypeRequest
        """
        self.set_resource_pool_name(resource_pool_name)
        return self

    def get_resource_type_name(self):
        """
        リソースタイプを取得
        :return: リソースタイプ
        :rtype: unicode
        """
        return self.__resource_type_name

    def set_resource_type_name(self, resource_type_name):
        """
        リソースタイプを設定
        :param resource_type_name: リソースタイプ
        :type resource_type_name: unicode
        """
        if resource_type_name is not None and not (isinstance(resource_type_name, str) or isinstance(resource_type_name, unicode)):
            raise TypeError(type(resource_type_name))
        self.__resource_type_name = resource_type_name

    def with_resource_type_name(self, resource_type_name):
        """
        リソースタイプを設定
        :param resource_type_name: リソースタイプ
        :type resource_type_name: unicode
        :return: this
        :rtype: IncreaseExperienceByUserIdAndResourceTypeRequest
        """
        self.set_resource_type_name(resource_type_name)
        return self

    def get_resource_id(self):
        """
        リソースIDを取得
        :return: リソースID
        :rtype: unicode
        """
        return self.__resource_id

    def set_resource_id(self, resource_id):
        """
        リソースIDを設定
        :param resource_id: リソースID
        :type resource_id: unicode
        """
        if resource_id is not None and not (isinstance(resource_id, str) or isinstance(resource_id, unicode)):
            raise TypeError(type(resource_id))
        self.__resource_id = resource_id

    def with_resource_id(self, resource_id):
        """
        リソースIDを設定
        :param resource_id: リソースID
        :type resource_id: unicode
        :return: this
        :rtype: IncreaseExperienceByUserIdAndResourceTypeRequest
        """
        self.set_resource_id(resource_id)
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
        if user_id is not None and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ステータスを設定
        :param user_id: ステータス
        :type user_id: unicode
        :return: this
        :rtype: IncreaseExperienceByUserIdAndResourceTypeRequest
        """
        self.set_user_id(user_id)
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
        if value is not None and not (isinstance(value, int) or isinstance(value, long)):
            raise TypeError(type(value))
        self.__value = value

    def with_value(self, value):
        """
        経験値の加算量を設定
        :param value: 経験値の加算量
        :type value: long
        :return: this
        :rtype: IncreaseExperienceByUserIdAndResourceTypeRequest
        """
        self.set_value(value)
        return self
