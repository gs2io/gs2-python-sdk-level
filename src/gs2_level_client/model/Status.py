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


class Status(object):

    def __init__(self, params=None):
        if params is None:
            self.__status_id = None
            self.__resource_type_name = None
            self.__user_id = None
            self.__resource_id = None
            self.__level = None
            self.__level_cap = None
            self.__experience = None
            self.__next_level_experience = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_status_id(params['statusId'] if 'statusId' in params.keys() else None)
            self.set_resource_type_name(params['resourceTypeName'] if 'resourceTypeName' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_resource_id(params['resourceId'] if 'resourceId' in params.keys() else None)
            self.set_level(params['level'] if 'level' in params.keys() else None)
            self.set_level_cap(params['levelCap'] if 'levelCap' in params.keys() else None)
            self.set_experience(params['experience'] if 'experience' in params.keys() else None)
            self.set_next_level_experience(params['nextLevelExperience'] if 'nextLevelExperience' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_status_id(self):
        """
        ステータスGRNを取得
        :return: ステータスGRN
        :rtype: unicode
        """
        return self.__status_id

    def set_status_id(self, status_id):
        """
        ステータスGRNを設定
        :param status_id: ステータスGRN
        :type status_id: unicode
        """
        self.__status_id = status_id

    def get_resource_type_name(self):
        """
        リソースタイプ名を取得
        :return: リソースタイプ名
        :rtype: unicode
        """
        return self.__resource_type_name

    def set_resource_type_name(self, resource_type_name):
        """
        リソースタイプ名を設定
        :param resource_type_name: リソースタイプ名
        :type resource_type_name: unicode
        """
        self.__resource_type_name = resource_type_name

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

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
        self.__resource_id = resource_id

    def get_level(self):
        """
        レベルを取得
        :return: レベル
        :rtype: int
        """
        return self.__level

    def set_level(self, level):
        """
        レベルを設定
        :param level: レベル
        :type level: int
        """
        self.__level = level

    def get_level_cap(self):
        """
        レベルキャップを取得
        :return: レベルキャップ
        :rtype: int
        """
        return self.__level_cap

    def set_level_cap(self, level_cap):
        """
        レベルキャップを設定
        :param level_cap: レベルキャップ
        :type level_cap: int
        """
        self.__level_cap = level_cap

    def get_experience(self):
        """
        累計獲得経験値を取得
        :return: 累計獲得経験値
        :rtype: long
        """
        return self.__experience

    def set_experience(self, experience):
        """
        累計獲得経験値を設定
        :param experience: 累計獲得経験値
        :type experience: long
        """
        self.__experience = experience

    def get_next_level_experience(self):
        """
        次のレベルに上がる累計獲得経験値を取得
        :return: 次のレベルに上がる累計獲得経験値
        :rtype: long
        """
        return self.__next_level_experience

    def set_next_level_experience(self, next_level_experience):
        """
        次のレベルに上がる累計獲得経験値を設定
        :param next_level_experience: 次のレベルに上がる累計獲得経験値
        :type next_level_experience: long
        """
        self.__next_level_experience = next_level_experience

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Status, self).__getitem__(key)

    def to_dict(self):
        return {
            "statusId": self.__status_id,
            "resourceTypeName": self.__resource_type_name,
            "userId": self.__user_id,
            "resourceId": self.__resource_id,
            "level": self.__level,
            "levelCap": self.__level_cap,
            "experience": self.__experience,
            "nextLevelExperience": self.__next_level_experience,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
