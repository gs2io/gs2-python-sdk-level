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


class ChangeLevelCapByUserIdAndResourceTypeRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "ChangeLevelCapByUserId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ChangeLevelCapByUserIdAndResourceTypeRequest, self).__init__(params)
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
            self.__level_cap = None
        else:
            self.set_level_cap(params['levelCap'] if 'levelCap' in params.keys() else None)

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
        :rtype: ChangeLevelCapByUserIdAndResourceTypeRequest
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
        :rtype: ChangeLevelCapByUserIdAndResourceTypeRequest
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
        :rtype: ChangeLevelCapByUserIdAndResourceTypeRequest
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
        :rtype: ChangeLevelCapByUserIdAndResourceTypeRequest
        """
        self.set_user_id(user_id)
        return self

    def get_level_cap(self):
        """
        新しいレベルキャップを取得
        :return: 新しいレベルキャップ
        :rtype: int
        """
        return self.__level_cap

    def set_level_cap(self, level_cap):
        """
        新しいレベルキャップを設定
        :param level_cap: 新しいレベルキャップ
        :type level_cap: int
        """
        if level_cap is not None and not isinstance(level_cap, int):
            raise TypeError(type(level_cap))
        self.__level_cap = level_cap

    def with_level_cap(self, level_cap):
        """
        新しいレベルキャップを設定
        :param level_cap: 新しいレベルキャップ
        :type level_cap: int
        :return: this
        :rtype: ChangeLevelCapByUserIdAndResourceTypeRequest
        """
        self.set_level_cap(level_cap)
        return self
