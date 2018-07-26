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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_level_client.Gs2Level import Gs2Level


class DescribeStatusRequest(Gs2UserRequest):

    class Constant(Gs2Level):
        FUNCTION = "DescribeStatus"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeStatusRequest, self).__init__(params)
        if params is None:
            self.__resource_pool_name = None
            self.__status_ids = None
            self.__page_token = None
            self.__limit = None
        else:
            self.set_resource_pool_name(params['resourcePoolName'] if 'resourcePoolName' in params.keys() else None)
            self.set_status_ids(params['statusIds'] if 'statusIds' in params.keys() else None)
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

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
        :rtype: DescribeStatusRequest
        """
        self.set_resource_pool_name(resource_pool_name)
        return self

    def get_status_ids(self):
        """
        ステータスIDリスト(カンマ区切り)を取得
        :return: ステータスIDリスト(カンマ区切り)
        :rtype: unicode
        """
        return self.__status_ids

    def set_status_ids(self, status_ids):
        """
        ステータスIDリスト(カンマ区切り)を設定
        :param status_ids: ステータスIDリスト(カンマ区切り)
        :type status_ids: unicode
        """
        if status_ids and not (isinstance(status_ids, str) or isinstance(status_ids, unicode)):
            raise TypeError(type(status_ids))
        self.__status_ids = status_ids

    def with_status_ids(self, status_ids):
        """
        ステータスIDリスト(カンマ区切り)を設定
        :param status_ids: ステータスIDリスト(カンマ区切り)
        :type status_ids: unicode
        :return: this
        :rtype: DescribeStatusRequest
        """
        self.set_status_ids(status_ids)
        return self

    def get_page_token(self):
        """
        データの取得を開始する位置を指定するトークンを取得
        :return: データの取得を開始する位置を指定するトークン
        :rtype: unicode
        """
        return self.__page_token

    def set_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        """
        if page_token and not (isinstance(page_token, str) or isinstance(page_token, unicode)):
            raise TypeError(type(page_token))
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: DescribeStatusRequest
        """
        self.set_page_token(page_token)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        if limit and not isinstance(limit, int):
            raise TypeError(type(limit))
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeStatusRequest
        """
        self.set_limit(limit)
        return self
