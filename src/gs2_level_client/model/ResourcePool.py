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


class ResourcePool(object):

    def __init__(self, params=None):
        if params is None:
            self.__resource_pool_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__service_class = None
            self.__level_cap_script = None
            self.__change_experience_trigger_script = None
            self.__change_experience_done_trigger_script = None
            self.__change_level_trigger_script = None
            self.__change_level_done_trigger_script = None
            self.__change_level_cap_trigger_script = None
            self.__change_level_cap_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_resource_pool_id(params['resourcePoolId'] if 'resourcePoolId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_level_cap_script(params['levelCapScript'] if 'levelCapScript' in params.keys() else None)
            self.set_change_experience_trigger_script(params['changeExperienceTriggerScript'] if 'changeExperienceTriggerScript' in params.keys() else None)
            self.set_change_experience_done_trigger_script(params['changeExperienceDoneTriggerScript'] if 'changeExperienceDoneTriggerScript' in params.keys() else None)
            self.set_change_level_trigger_script(params['changeLevelTriggerScript'] if 'changeLevelTriggerScript' in params.keys() else None)
            self.set_change_level_done_trigger_script(params['changeLevelDoneTriggerScript'] if 'changeLevelDoneTriggerScript' in params.keys() else None)
            self.set_change_level_cap_trigger_script(params['changeLevelCapTriggerScript'] if 'changeLevelCapTriggerScript' in params.keys() else None)
            self.set_change_level_cap_done_trigger_script(params['changeLevelCapDoneTriggerScript'] if 'changeLevelCapDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_resource_pool_id(self):
        """
        リソースプールGRNを取得
        :return: リソースプールGRN
        :rtype: unicode
        """
        return self.__resource_pool_id

    def set_resource_pool_id(self, resource_pool_id):
        """
        リソースプールGRNを設定
        :param resource_pool_id: リソースプールGRN
        :type resource_pool_id: unicode
        """
        self.__resource_pool_id = resource_pool_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_name(self):
        """
        リソースプール名を取得
        :return: リソースプール名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        リソースプール名を設定
        :param name: リソースプール名
        :type name: unicode
        """
        self.__name = name

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def get_level_cap_script(self):
        """
        レベルキャップ取得時 に実行されるGS2-Scriptを取得
        :return: レベルキャップ取得時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__level_cap_script

    def set_level_cap_script(self, level_cap_script):
        """
        レベルキャップ取得時 に実行されるGS2-Scriptを設定
        :param level_cap_script: レベルキャップ取得時 に実行されるGS2-Script
        :type level_cap_script: unicode
        """
        self.__level_cap_script = level_cap_script

    def get_change_experience_trigger_script(self):
        """
        経験値変化時 に実行されるGS2-Scriptを取得
        :return: 経験値変化時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__change_experience_trigger_script

    def set_change_experience_trigger_script(self, change_experience_trigger_script):
        """
        経験値変化時 に実行されるGS2-Scriptを設定
        :param change_experience_trigger_script: 経験値変化時 に実行されるGS2-Script
        :type change_experience_trigger_script: unicode
        """
        self.__change_experience_trigger_script = change_experience_trigger_script

    def get_change_experience_done_trigger_script(self):
        """
        経験値変化完了時 に実行されるGS2-Scriptを取得
        :return: 経験値変化完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__change_experience_done_trigger_script

    def set_change_experience_done_trigger_script(self, change_experience_done_trigger_script):
        """
        経験値変化完了時 に実行されるGS2-Scriptを設定
        :param change_experience_done_trigger_script: 経験値変化完了時 に実行されるGS2-Script
        :type change_experience_done_trigger_script: unicode
        """
        self.__change_experience_done_trigger_script = change_experience_done_trigger_script

    def get_change_level_trigger_script(self):
        """
        レベル変化時 に実行されるGS2-Scriptを取得
        :return: レベル変化時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__change_level_trigger_script

    def set_change_level_trigger_script(self, change_level_trigger_script):
        """
        レベル変化時 に実行されるGS2-Scriptを設定
        :param change_level_trigger_script: レベル変化時 に実行されるGS2-Script
        :type change_level_trigger_script: unicode
        """
        self.__change_level_trigger_script = change_level_trigger_script

    def get_change_level_done_trigger_script(self):
        """
        レベル変化完了時 に実行されるGS2-Scriptを取得
        :return: レベル変化完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__change_level_done_trigger_script

    def set_change_level_done_trigger_script(self, change_level_done_trigger_script):
        """
        レベル変化完了時 に実行されるGS2-Scriptを設定
        :param change_level_done_trigger_script: レベル変化完了時 に実行されるGS2-Script
        :type change_level_done_trigger_script: unicode
        """
        self.__change_level_done_trigger_script = change_level_done_trigger_script

    def get_change_level_cap_trigger_script(self):
        """
        レベルキャップ変化時 に実行されるGS2-Scriptを取得
        :return: レベルキャップ変化時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__change_level_cap_trigger_script

    def set_change_level_cap_trigger_script(self, change_level_cap_trigger_script):
        """
        レベルキャップ変化時 に実行されるGS2-Scriptを設定
        :param change_level_cap_trigger_script: レベルキャップ変化時 に実行されるGS2-Script
        :type change_level_cap_trigger_script: unicode
        """
        self.__change_level_cap_trigger_script = change_level_cap_trigger_script

    def get_change_level_cap_done_trigger_script(self):
        """
        レベルキャップ変化完了時 に実行されるGS2-Scriptを取得
        :return: レベルキャップ変化完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__change_level_cap_done_trigger_script

    def set_change_level_cap_done_trigger_script(self, change_level_cap_done_trigger_script):
        """
        レベルキャップ変化完了時 に実行されるGS2-Scriptを設定
        :param change_level_cap_done_trigger_script: レベルキャップ変化完了時 に実行されるGS2-Script
        :type change_level_cap_done_trigger_script: unicode
        """
        self.__change_level_cap_done_trigger_script = change_level_cap_done_trigger_script

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
        return super(ResourcePool, self).__getitem__(key)

    def to_dict(self):
        return {
            "resourcePoolId": self.__resource_pool_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "serviceClass": self.__service_class,
            "levelCapScript": self.__level_cap_script,
            "changeExperienceTriggerScript": self.__change_experience_trigger_script,
            "changeExperienceDoneTriggerScript": self.__change_experience_done_trigger_script,
            "changeLevelTriggerScript": self.__change_level_trigger_script,
            "changeLevelDoneTriggerScript": self.__change_level_done_trigger_script,
            "changeLevelCapTriggerScript": self.__change_level_cap_trigger_script,
            "changeLevelCapDoneTriggerScript": self.__change_level_cap_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
