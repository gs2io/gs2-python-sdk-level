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


class UpdateResourceTypeMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "UpdateResourceTypeMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateResourceTypeMasterRequest, self).__init__(params)
        if params is None:
            self.__resource_pool_name = None
        else:
            self.set_resource_pool_name(params['resourcePoolName'] if 'resourcePoolName' in params.keys() else None)
        if params is None:
            self.__resource_type_name = None
        else:
            self.set_resource_type_name(params['resourceTypeName'] if 'resourceTypeName' in params.keys() else None)
        if params is None:
            self.__meta = None
        else:
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
        if params is None:
            self.__level_table_name = None
        else:
            self.set_level_table_name(params['levelTableName'] if 'levelTableName' in params.keys() else None)
        if params is None:
            self.__default_experience = None
        else:
            self.set_default_experience(params['defaultExperience'] if 'defaultExperience' in params.keys() else None)
        if params is None:
            self.__default_level_cap = None
        else:
            self.set_default_level_cap(params['defaultLevelCap'] if 'defaultLevelCap' in params.keys() else None)
        if params is None:
            self.__max_level_cap = None
        else:
            self.set_max_level_cap(params['maxLevelCap'] if 'maxLevelCap' in params.keys() else None)

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
        :rtype: UpdateResourceTypeMasterRequest
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
        :rtype: UpdateResourceTypeMasterRequest
        """
        self.set_resource_type_name(resource_type_name)
        return self

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
        if meta and not (isinstance(meta, str) or isinstance(meta, unicode)):
            raise TypeError(type(meta))
        self.__meta = meta

    def with_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        :return: this
        :rtype: UpdateResourceTypeMasterRequest
        """
        self.set_meta(meta)
        return self

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
        if level_table_name and not (isinstance(level_table_name, str) or isinstance(level_table_name, unicode)):
            raise TypeError(type(level_table_name))
        self.__level_table_name = level_table_name

    def with_level_table_name(self, level_table_name):
        """
        レベルテーブル名を設定
        :param level_table_name: レベルテーブル名
        :type level_table_name: unicode
        :return: this
        :rtype: UpdateResourceTypeMasterRequest
        """
        self.set_level_table_name(level_table_name)
        return self

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
        if default_experience and not (isinstance(default_experience, int) or isinstance(default_experience, long)):
            raise TypeError(type(default_experience))
        self.__default_experience = default_experience

    def with_default_experience(self, default_experience):
        """
        デフォルト取得済み経験値を設定
        :param default_experience: デフォルト取得済み経験値
        :type default_experience: long
        :return: this
        :rtype: UpdateResourceTypeMasterRequest
        """
        self.set_default_experience(default_experience)
        return self

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
        if default_level_cap and not isinstance(default_level_cap, int):
            raise TypeError(type(default_level_cap))
        self.__default_level_cap = default_level_cap

    def with_default_level_cap(self, default_level_cap):
        """
        デフォルトレベルキャップを設定
        :param default_level_cap: デフォルトレベルキャップ
        :type default_level_cap: int
        :return: this
        :rtype: UpdateResourceTypeMasterRequest
        """
        self.set_default_level_cap(default_level_cap)
        return self

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
        if max_level_cap and not isinstance(max_level_cap, int):
            raise TypeError(type(max_level_cap))
        self.__max_level_cap = max_level_cap

    def with_max_level_cap(self, max_level_cap):
        """
        最大レベルキャップを設定
        :param max_level_cap: 最大レベルキャップ
        :type max_level_cap: int
        :return: this
        :rtype: UpdateResourceTypeMasterRequest
        """
        self.set_max_level_cap(max_level_cap)
        return self
