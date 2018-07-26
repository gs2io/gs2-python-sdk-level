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


class LevelTableMaster(object):

    def __init__(self, params=None):
        if params is None:
            self.__level_table_id = None
            self.__name = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_level_table_id(params['levelTableId'] if 'levelTableId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_level_table_id(self):
        """
        レベルテーブルGRNを取得
        :return: レベルテーブルGRN
        :rtype: unicode
        """
        return self.__level_table_id

    def set_level_table_id(self, level_table_id):
        """
        レベルテーブルGRNを設定
        :param level_table_id: レベルテーブルGRN
        :type level_table_id: unicode
        """
        self.__level_table_id = level_table_id

    def get_name(self):
        """
        レベルテーブル名を取得
        :return: レベルテーブル名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        レベルテーブル名を設定
        :param name: レベルテーブル名
        :type name: unicode
        """
        self.__name = name

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
        return super(LevelTableMaster, self).__getitem__(key)

    def to_dict(self):
        return {
            "levelTableId": self.__level_table_id,
            "name": self.__name,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
