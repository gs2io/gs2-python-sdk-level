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


class LevelThresholdMaster(object):

    def __init__(self, params=None):
        if params is None:
            self.__threshold_id = None
            self.__threshold = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_threshold_id(params['thresholdId'] if 'thresholdId' in params.keys() else None)
            self.set_threshold(params['threshold'] if 'threshold' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_threshold_id(self):
        """
        レベルアップ経験値閾値GRNを取得
        :return: レベルアップ経験値閾値GRN
        :rtype: unicode
        """
        return self.__threshold_id

    def set_threshold_id(self, threshold_id):
        """
        レベルアップ経験値閾値GRNを設定
        :param threshold_id: レベルアップ経験値閾値GRN
        :type threshold_id: unicode
        """
        self.__threshold_id = threshold_id

    def get_threshold(self):
        """
        レベルアップ経験値閾値を取得
        :return: レベルアップ経験値閾値
        :rtype: long
        """
        return self.__threshold

    def set_threshold(self, threshold):
        """
        レベルアップ経験値閾値を設定
        :param threshold: レベルアップ経験値閾値
        :type threshold: long
        """
        self.__threshold = threshold

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
        return super(LevelThresholdMaster, self).__getitem__(key)

    def to_dict(self):
        return {
            "thresholdId": self.__threshold_id,
            "threshold": self.__threshold,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
