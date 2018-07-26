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


class CreateResourcePoolRequest(Gs2BasicRequest):

    class Constant(Gs2Level):
        FUNCTION = "CreateResourcePool"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateResourcePoolRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__service_class = None
        else:
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
        if params is None:
            self.__level_cap_script = None
        else:
            self.set_level_cap_script(params['levelCapScript'] if 'levelCapScript' in params.keys() else None)
        if params is None:
            self.__change_experience_trigger_script = None
        else:
            self.set_change_experience_trigger_script(params['changeExperienceTriggerScript'] if 'changeExperienceTriggerScript' in params.keys() else None)
        if params is None:
            self.__change_experience_done_trigger_script = None
        else:
            self.set_change_experience_done_trigger_script(params['changeExperienceDoneTriggerScript'] if 'changeExperienceDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__change_level_trigger_script = None
        else:
            self.set_change_level_trigger_script(params['changeLevelTriggerScript'] if 'changeLevelTriggerScript' in params.keys() else None)
        if params is None:
            self.__change_level_done_trigger_script = None
        else:
            self.set_change_level_done_trigger_script(params['changeLevelDoneTriggerScript'] if 'changeLevelDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__change_level_cap_trigger_script = None
        else:
            self.set_change_level_cap_trigger_script(params['changeLevelCapTriggerScript'] if 'changeLevelCapTriggerScript' in params.keys() else None)
        if params is None:
            self.__change_level_cap_done_trigger_script = None
        else:
            self.set_change_level_cap_done_trigger_script(params['changeLevelCapDoneTriggerScript'] if 'changeLevelCapDoneTriggerScript' in params.keys() else None)

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
        if name and not (isinstance(name, str) or isinstance(name, unicode)):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        リソースプール名を設定
        :param name: リソースプール名
        :type name: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_name(name)
        return self

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
        if description and not (isinstance(description, str) or isinstance(description, unicode)):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_description(description)
        return self

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
        if service_class and not (isinstance(service_class, str) or isinstance(service_class, unicode)):
            raise TypeError(type(service_class))
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_service_class(service_class)
        return self

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
        if level_cap_script and not (isinstance(level_cap_script, str) or isinstance(level_cap_script, unicode)):
            raise TypeError(type(level_cap_script))
        self.__level_cap_script = level_cap_script

    def with_level_cap_script(self, level_cap_script):
        """
        レベルキャップ取得時 に実行されるGS2-Scriptを設定
        :param level_cap_script: レベルキャップ取得時 に実行されるGS2-Script
        :type level_cap_script: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_level_cap_script(level_cap_script)
        return self

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
        if change_experience_trigger_script and not (isinstance(change_experience_trigger_script, str) or isinstance(change_experience_trigger_script, unicode)):
            raise TypeError(type(change_experience_trigger_script))
        self.__change_experience_trigger_script = change_experience_trigger_script

    def with_change_experience_trigger_script(self, change_experience_trigger_script):
        """
        経験値変化時 に実行されるGS2-Scriptを設定
        :param change_experience_trigger_script: 経験値変化時 に実行されるGS2-Script
        :type change_experience_trigger_script: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_change_experience_trigger_script(change_experience_trigger_script)
        return self

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
        if change_experience_done_trigger_script and not (isinstance(change_experience_done_trigger_script, str) or isinstance(change_experience_done_trigger_script, unicode)):
            raise TypeError(type(change_experience_done_trigger_script))
        self.__change_experience_done_trigger_script = change_experience_done_trigger_script

    def with_change_experience_done_trigger_script(self, change_experience_done_trigger_script):
        """
        経験値変化完了時 に実行されるGS2-Scriptを設定
        :param change_experience_done_trigger_script: 経験値変化完了時 に実行されるGS2-Script
        :type change_experience_done_trigger_script: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_change_experience_done_trigger_script(change_experience_done_trigger_script)
        return self

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
        if change_level_trigger_script and not (isinstance(change_level_trigger_script, str) or isinstance(change_level_trigger_script, unicode)):
            raise TypeError(type(change_level_trigger_script))
        self.__change_level_trigger_script = change_level_trigger_script

    def with_change_level_trigger_script(self, change_level_trigger_script):
        """
        レベル変化時 に実行されるGS2-Scriptを設定
        :param change_level_trigger_script: レベル変化時 に実行されるGS2-Script
        :type change_level_trigger_script: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_change_level_trigger_script(change_level_trigger_script)
        return self

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
        if change_level_done_trigger_script and not (isinstance(change_level_done_trigger_script, str) or isinstance(change_level_done_trigger_script, unicode)):
            raise TypeError(type(change_level_done_trigger_script))
        self.__change_level_done_trigger_script = change_level_done_trigger_script

    def with_change_level_done_trigger_script(self, change_level_done_trigger_script):
        """
        レベル変化完了時 に実行されるGS2-Scriptを設定
        :param change_level_done_trigger_script: レベル変化完了時 に実行されるGS2-Script
        :type change_level_done_trigger_script: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_change_level_done_trigger_script(change_level_done_trigger_script)
        return self

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
        if change_level_cap_trigger_script and not (isinstance(change_level_cap_trigger_script, str) or isinstance(change_level_cap_trigger_script, unicode)):
            raise TypeError(type(change_level_cap_trigger_script))
        self.__change_level_cap_trigger_script = change_level_cap_trigger_script

    def with_change_level_cap_trigger_script(self, change_level_cap_trigger_script):
        """
        レベルキャップ変化時 に実行されるGS2-Scriptを設定
        :param change_level_cap_trigger_script: レベルキャップ変化時 に実行されるGS2-Script
        :type change_level_cap_trigger_script: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_change_level_cap_trigger_script(change_level_cap_trigger_script)
        return self

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
        if change_level_cap_done_trigger_script and not (isinstance(change_level_cap_done_trigger_script, str) or isinstance(change_level_cap_done_trigger_script, unicode)):
            raise TypeError(type(change_level_cap_done_trigger_script))
        self.__change_level_cap_done_trigger_script = change_level_cap_done_trigger_script

    def with_change_level_cap_done_trigger_script(self, change_level_cap_done_trigger_script):
        """
        レベルキャップ変化完了時 に実行されるGS2-Scriptを設定
        :param change_level_cap_done_trigger_script: レベルキャップ変化完了時 に実行されるGS2-Script
        :type change_level_cap_done_trigger_script: unicode
        :return: this
        :rtype: CreateResourcePoolRequest
        """
        self.set_change_level_cap_done_trigger_script(change_level_cap_done_trigger_script)
        return self
