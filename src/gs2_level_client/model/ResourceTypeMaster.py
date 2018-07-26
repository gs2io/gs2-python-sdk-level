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


class ResourceTypeMaster(object):

    def __init__(self, params=None):
        if params is None:
            self.__resource_type_id = None
            self.__name = None
            self.__meta = None
            self.__level_table_name = None
            self.__default_experience = None
            self.__default_level_cap = None
            self.__max_level_cap = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_resource_type_id(params['resourceTypeId'] if 'resourceTypeId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
            self.set_level_table_name(params['levelTableName'] if 'levelTableName' in params.keys() else None)
            self.set_default_experience(params['defaultExperience'] if 'defaultExperience' in params.keys() else None)
            self.set_default_level_cap(params['defaultLevelCap'] if 'defaultLevelCap' in params.keys() else None)
            self.set_max_level_cap(params['maxLevelCap'] if 'maxLevelCap' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_resource_type_id(self):
        """
        リソースタイプGRNを取得
        :return: リソースタイプGRN
        :rtype: unicode
        """
        return self.__resource_type_id

    def set_resource_type_id(self, resource_type_id):
        """
        リソースタイプGRNを設定
        :param resource_type_id: リソースタイプGRN
        :type resource_type_id: unicode
        """
        self.__resource_type_id = resource_type_id

    def get_name(self):
        """
        リソースタイプ名を取得
        :return: リソースタイプ名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        リソースタイプ名を設定
        :param name: リソースタイプ名
        :type name: unicode
        """
        self.__name = name

    def get_meta(self):
        """
        メタデータを取得
        :return: メタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        """
        self.__meta = meta

    def get_level_table_name(self):
        """
        レベルテーブル名を取得
        :return: レベルテーブル名
        :rtype: unicode
        """
        return self.__level_table_name

    def set_level_table_name(self, level_table_name):
        """
        レベルテーブル名を設定
        :param level_table_name: レベルテーブル名
        :type level_table_name: unicode
        """
        self.__level_table_name = level_table_name

    def get_default_experience(self):
        """
        デフォルト取得済み経験値を取得
        :return: デフォルト取得済み経験値
        :rtype: long
        """
        return self.__default_experience

    def set_default_experience(self, default_experience):
        """
        デフォルト取得済み経験値を設定
        :param default_experience: デフォルト取得済み経験値
        :type default_experience: long
        """
        self.__default_experience = default_experience

    def get_default_level_cap(self):
        """
        デフォルトレベルキャップを取得
        :return: デフォルトレベルキャップ
        :rtype: int
        """
        return self.__default_level_cap

    def set_default_level_cap(self, default_level_cap):
        """
        デフォルトレベルキャップを設定
        :param default_level_cap: デフォルトレベルキャップ
        :type default_level_cap: int
        """
        self.__default_level_cap = default_level_cap

    def get_max_level_cap(self):
        """
        最大レベルキャップを取得
        :return: 最大レベルキャップ
        :rtype: int
        """
        return self.__max_level_cap

    def set_max_level_cap(self, max_level_cap):
        """
        最大レベルキャップを設定
        :param max_level_cap: 最大レベルキャップ
        :type max_level_cap: int
        """
        self.__max_level_cap = max_level_cap

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
        return super(ResourceTypeMaster, self).__getitem__(key)

    def to_dict(self):
        return {
            "resourceTypeId": self.__resource_type_id,
            "name": self.__name,
            "meta": self.__meta,
            "levelTableName": self.__level_table_name,
            "defaultExperience": self.__default_experience,
            "defaultLevelCap": self.__default_level_cap,
            "maxLevelCap": self.__max_level_cap,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
