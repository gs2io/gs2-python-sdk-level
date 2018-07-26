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


class SetExperienceByUserIdAndResourceTypeRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "SetExperienceByUserId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(SetExperienceByUserIdAndResourceTypeRequest, self).__init__(params)
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
            self.__experience = None
        else:
            self.set_experience(params['experience'] if 'experience' in params.keys() else None)

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
        :rtype: SetExperienceByUserIdAndResourceTypeRequest
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
        if resource_type_name and not (isinstance(resource_type_name, str) or isinstance(resource_type_name, unicode)):
            raise TypeError(type(resource_type_name))
        self.__resource_type_name = resource_type_name

    def with_resource_type_name(self, resource_type_name):
        """
        リソースタイプを設定
        :param resource_type_name: リソースタイプ
        :type resource_type_name: unicode
        :return: this
        :rtype: SetExperienceByUserIdAndResourceTypeRequest
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
        if resource_id and not (isinstance(resource_id, str) or isinstance(resource_id, unicode)):
            raise TypeError(type(resource_id))
        self.__resource_id = resource_id

    def with_resource_id(self, resource_id):
        """
        リソースIDを設定
        :param resource_id: リソースID
        :type resource_id: unicode
        :return: this
        :rtype: SetExperienceByUserIdAndResourceTypeRequest
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
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ステータスを設定
        :param user_id: ステータス
        :type user_id: unicode
        :return: this
        :rtype: SetExperienceByUserIdAndResourceTypeRequest
        """
        self.set_user_id(user_id)
        return self

    def get_experience(self):
        """
        新しい累計獲得経験値を取得
        :return: 新しい累計獲得経験値
        :rtype: long
        """
        return self.__experience

    def set_experience(self, experience):
        """
        新しい累計獲得経験値を設定
        :param experience: 新しい累計獲得経験値
        :type experience: long
        """
        if experience and not (isinstance(experience, int) or isinstance(experience, long)):
            raise TypeError(type(experience))
        self.__experience = experience

    def with_experience(self, experience):
        """
        新しい累計獲得経験値を設定
        :param experience: 新しい累計獲得経験値
        :type experience: long
        :return: this
        :rtype: SetExperienceByUserIdAndResourceTypeRequest
        """
        self.set_experience(experience)
        return self
