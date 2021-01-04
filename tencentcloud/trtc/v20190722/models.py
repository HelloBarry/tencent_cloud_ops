# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class AbnormalEvent(AbstractModel):
    """造成异常体验可能的异常事件类型

    """

    def __init__(self):
        """
        :param AbnormalEventId: 异常事件ID，具体值查看附录：异常体验ID映射表：https://cloud.tencent.com/document/product/647/44916
        :type AbnormalEventId: int
        :param PeerId: 远端用户ID,""：表示异常事件不是由远端用户产生
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerId: str
        """
        self.AbnormalEventId = None
        self.PeerId = None


    def _deserialize(self, params):
        self.AbnormalEventId = params.get("AbnormalEventId")
        self.PeerId = params.get("PeerId")


class AbnormalExperience(AbstractModel):
    """用户的异常体验及可能的原因

    """

    def __init__(self):
        """
        :param UserId: 用户ID
        :type UserId: str
        :param ExperienceId: 异常体验ID
        :type ExperienceId: int
        :param RoomId: 字符串房间号
        :type RoomId: str
        :param AbnormalEventList: 异常事件数组
        :type AbnormalEventList: list of AbnormalEvent
        :param EventTime: 异常事件的上报时间
        :type EventTime: int
        """
        self.UserId = None
        self.ExperienceId = None
        self.RoomId = None
        self.AbnormalEventList = None
        self.EventTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.ExperienceId = params.get("ExperienceId")
        self.RoomId = params.get("RoomId")
        if params.get("AbnormalEventList") is not None:
            self.AbnormalEventList = []
            for item in params.get("AbnormalEventList"):
                obj = AbnormalEvent()
                obj._deserialize(item)
                self.AbnormalEventList.append(obj)
        self.EventTime = params.get("EventTime")


class CreateTroubleInfoRequest(AbstractModel):
    """CreateTroubleInfo请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 应用的ID
        :type SdkAppId: str
        :param RoomId: 房间ID
        :type RoomId: str
        :param TeacherUserId: 老师用户ID
        :type TeacherUserId: str
        :param StudentUserId: 学生用户ID
        :type StudentUserId: str
        :param TroubleUserId: 体验异常端（老师或学生）的用户 ID。
        :type TroubleUserId: str
        :param TroubleType: 异常类型。
1. 仅视频异常
2. 仅声音异常
3. 音视频都异常
5. 进房异常
4. 切课
6. 求助
7. 问题反馈
8. 投诉
        :type TroubleType: int
        :param TroubleTime: 异常发生的UNIX 时间戳，单位为秒。
        :type TroubleTime: int
        :param TroubleMsg: 异常详情
        :type TroubleMsg: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.TeacherUserId = None
        self.StudentUserId = None
        self.TroubleUserId = None
        self.TroubleType = None
        self.TroubleTime = None
        self.TroubleMsg = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.TeacherUserId = params.get("TeacherUserId")
        self.StudentUserId = params.get("StudentUserId")
        self.TroubleUserId = params.get("TroubleUserId")
        self.TroubleType = params.get("TroubleType")
        self.TroubleTime = params.get("TroubleTime")
        self.TroubleMsg = params.get("TroubleMsg")


class CreateTroubleInfoResponse(AbstractModel):
    """CreateTroubleInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAbnormalEventRequest(AbstractModel):
    """DescribeAbnormalEvent请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 用户SDKAppID，查询SDKAppID下任意20条异常体验事件（可能不同房间）
        :type SdkAppId: str
        :param StartTime: 查询开始时间
        :type StartTime: int
        :param EndTime: 查询结束时间
        :type EndTime: int
        :param RoomId: 房间号，查询房间内任意20条以内异常体验事件
        :type RoomId: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")


class DescribeAbnormalEventResponse(AbstractModel):
    """DescribeAbnormalEvent返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 返回的数据总条数
        :type Total: int
        :param AbnormalExperienceList: 异常体验列表
        :type AbnormalExperienceList: list of AbnormalExperience
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.AbnormalExperienceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AbnormalExperienceList") is not None:
            self.AbnormalExperienceList = []
            for item in params.get("AbnormalExperienceList"):
                obj = AbnormalExperience()
                obj._deserialize(item)
                self.AbnormalExperienceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCallDetailRequest(AbstractModel):
    """DescribeCallDetail请求参数结构体

    """

    def __init__(self):
        """
        :param CommId: 通话 ID（唯一标识一次通话）： sdkappid_roomgString（房间号_createTime（房间创建时间，unix时间戳，单位为s）例：1400353843_218695_1590065777。通过 DescribeRoomInformation（查询房间列表）接口获取（链接：https://cloud.tencent.com/document/product/647/44050）
        :type CommId: str
        :param StartTime: 查询开始时间，14天内。本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        :param SdkAppId: 用户SDKAppID（1400188366）
        :type SdkAppId: str
        :param UserIds: 需查询的用户数组，不填默认返回6个用户,最多可填6个用户
        :type UserIds: list of str
        :param DataType: 需查询的指标，不填则只返回用户列表，填all则返回所有指标。
appCpu：APP CPU使用率；
sysCpu：系统 CPU使用率；
aBit：上/下行音频码率；
aBlock：音频卡顿时长；
bigvBit：上/下行视频码率；
bigvCapFps：视频采集帧率；
bigvEncFps：视频发送帧率；
bigvDecFps：渲染帧率；
bigvBlock：视频卡顿时长；
aLoss：上/下行音频丢包；
bigvLoss：上/下行视频丢包；
bigvWidth：上/下行分辨率宽；
bigvHeight：上/下行分辨率高
        :type DataType: list of str
        :param PageNumber: 设置分页index，从0开始（PageNumber和PageSize 其中一个不填均默认返回6条数据）
        :type PageNumber: str
        :param PageSize: 设置分页大小（PageNumber和PageSize 其中一个不填均默认返回6条数据,DataType，UserIds不为null，PageSize最大不超过6，DataType，UserIds为null，PageSize最大不超过100）
        :type PageSize: str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.DataType = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.DataType = params.get("DataType")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")


class DescribeCallDetailResponse(AbstractModel):
    """DescribeCallDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 返回的用户总条数
        :type Total: int
        :param UserList: 用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param Data: 质量数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of QualityData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDetailEventRequest(AbstractModel):
    """DescribeDetailEvent请求参数结构体

    """

    def __init__(self):
        """
        :param CommId: 通话 ID（唯一标识一次通话）： sdkappid_roomgString（房间号_createTime（房间创建时间，unix时间戳，单位s）。通过 DescribeRoomInformation（查询房间列表）接口获取。（链接：https://cloud.tencent.com/document/product/647/44050）
        :type CommId: str
        :param StartTime: 查询开始时间，14天内。本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        :param UserId: 用户id
        :type UserId: str
        :param RoomId: 房间号
        :type RoomId: str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.UserId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserId = params.get("UserId")
        self.RoomId = params.get("RoomId")


class DescribeDetailEventResponse(AbstractModel):
    """DescribeDetailEvent返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回的事件列表
        :type Data: list of EventList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = EventList()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryScaleRequest(AbstractModel):
    """DescribeHistoryScale请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param StartTime: 查询开始时间，5天内。本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeHistoryScaleResponse(AbstractModel):
    """DescribeHistoryScale返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 返回的数据条数
        :type Total: int
        :param ScaleList: 返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleList: list of ScaleInfomation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ScaleList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ScaleList") is not None:
            self.ScaleList = []
            for item in params.get("ScaleList"):
                obj = ScaleInfomation()
                obj._deserialize(item)
                self.ScaleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeNetworkRequest(AbstractModel):
    """DescribeRealtimeNetwork请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间，24小时内，本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param DataType: 需查询的数据类型
sendLossRateRaw：上行丢包率
recvLossRateRaw：下行丢包率
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeNetworkResponse(AbstractModel):
    """DescribeRealtimeNetwork返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 查询返回的数据
        :type Data: list of RealtimeData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeQualityRequest(AbstractModel):
    """DescribeRealtimeQuality请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间，24小时内。本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param DataType: 查询的数据类型
enterTotalSuccPercent：进房成功率
fistFreamInSecRate：首帧秒开率
blockPercent：视频卡顿率
audioBlockPercent：音频卡顿率
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeQualityResponse(AbstractModel):
    """DescribeRealtimeQuality返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回的数据类型
        :type Data: list of RealtimeData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeScaleRequest(AbstractModel):
    """DescribeRealtimeScale请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间，24小时内。本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param DataType: 查询的数据类型
UserNum：通话人数；
RoomNum：房间数
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeScaleResponse(AbstractModel):
    """DescribeRealtimeScale返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回的数据数组
        :type Data: list of RealtimeData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordStatisticRequest(AbstractModel):
    """DescribeRecordStatistic请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始日期。
        :type StartTime: str
        :param EndTime: 查询结束日期。
        :type EndTime: str
        :param SdkAppId: 应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")


class DescribeRecordStatisticResponse(AbstractModel):
    """DescribeRecordStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param SdkAppIdUsages: 应用的用量信息数组。
        :type SdkAppIdUsages: list of SdkAppIdRecordUsage
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SdkAppIdUsages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SdkAppIdUsages") is not None:
            self.SdkAppIdUsages = []
            for item in params.get("SdkAppIdUsages"):
                obj = SdkAppIdRecordUsage()
                obj._deserialize(item)
                self.SdkAppIdUsages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoomInformationRequest(AbstractModel):
    """DescribeRoomInformation请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param StartTime: 查询开始时间，14天内。本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        :param RoomId: 字符串房间号
        :type RoomId: str
        :param PageNumber: 分页index，从0开始（PageNumber和PageSize 其中一个不填均默认返回10条数据）
        :type PageNumber: str
        :param PageSize: 分页大小（PageNumber和PageSize 其中一个不填均默认返回10条数据,最大不超过100）
        :type PageSize: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")


class DescribeRoomInformationResponse(AbstractModel):
    """DescribeRoomInformation返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 返回当页数据总数
        :type Total: int
        :param RoomList: 房间信息列表
        :type RoomList: list of RoomState
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.RoomList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RoomList") is not None:
            self.RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self.RoomList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrtcInteractiveTimeRequest(AbstractModel):
    """DescribeTrtcInteractiveTime请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param SdkAppId: 应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回所有应用的合计值。
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")


class DescribeTrtcInteractiveTimeResponse(AbstractModel):
    """DescribeTrtcInteractiveTime返回参数结构体

    """

    def __init__(self):
        """
        :param Usages: 应用的用量信息数组。
        :type Usages: list of OneSdkAppIdUsagesInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = OneSdkAppIdUsagesInfo()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrtcMcuTranscodeTimeRequest(AbstractModel):
    """DescribeTrtcMcuTranscodeTime请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param SdkAppId: 应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")


class DescribeTrtcMcuTranscodeTimeResponse(AbstractModel):
    """DescribeTrtcMcuTranscodeTime返回参数结构体

    """

    def __init__(self):
        """
        :param Usages: 应用的用量信息数组。
        :type Usages: list of OneSdkAppIdTranscodeTimeUsagesInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = OneSdkAppIdTranscodeTimeUsagesInfo()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserInformationRequest(AbstractModel):
    """DescribeUserInformation请求参数结构体

    """

    def __init__(self):
        """
        :param CommId: 通话 ID（唯一标识一次通话）： sdkappid_roomgString（房间号_createTime（房间创建时间，unix时间戳，单位为s）例：1400353843_218695_1590065777。通过 DescribeRoomInformation（查询房间列表）接口获取（链接：https://cloud.tencent.com/document/product/647/44050）
        :type CommId: str
        :param StartTime: 查询开始时间，14天内。本地unix时间戳（1588031999s）
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳（1588031999s）
        :type EndTime: int
        :param SdkAppId: 用户SDKAppID（1400188366）
        :type SdkAppId: str
        :param UserIds: 需查询的用户数组，不填默认返回6个用户,最多可填6个用户
        :type UserIds: list of str
        :param PageNumber: 设置分页index，从0开始（PageNumber和PageSize 其中一个不填均默认返回6条数据）
        :type PageNumber: str
        :param PageSize: 设置分页大小（PageNumber和PageSize 其中一个不填均默认返回6条数据,PageSize最大不超过100）
        :type PageSize: str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")


class DescribeUserInformationResponse(AbstractModel):
    """DescribeUserInformation返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 返回的用户总条数
        :type Total: int
        :param UserList: 用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.RequestId = params.get("RequestId")


class DismissRoomByStrRoomIdRequest(AbstractModel):
    """DismissRoomByStrRoomId请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: str
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")


class DismissRoomByStrRoomIdResponse(AbstractModel):
    """DismissRoomByStrRoomId返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")


class DismissRoomResponse(AbstractModel):
    """DismissRoom返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncodeParams(AbstractModel):
    """MCU混流输出流编码参数

    """

    def __init__(self):
        """
        :param AudioSampleRate: 混流-输出流音频采样率。取值为[48000, 44100, 32000,24000,, 16000, 12000, 8000]，单位是Hz。
        :type AudioSampleRate: int
        :param AudioBitrate: 混流-输出流音频码率。取值范围[8,500]，单位为Kbps。
        :type AudioBitrate: int
        :param AudioChannels: 混流-输出流音频声道数，取值范围[1,2]，1表示混流输出音频为单声道，2表示混流输出音频为双声道。
        :type AudioChannels: int
        :param VideoWidth: 混流-输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :type VideoWidth: int
        :param VideoHeight: 混流-输出流高，音视频输出时必填。取值范围[0,1080]，单位为像素值。
        :type VideoHeight: int
        :param VideoBitrate: 混流-输出流码率，音视频输出时必填。取值范围[1,10000]，单位为Kbps。
        :type VideoBitrate: int
        :param VideoFramerate: 混流-输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :type VideoFramerate: int
        :param VideoGop: 混流-输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :type VideoGop: int
        :param BackgroundColor: 混流-输出流背景色。
        :type BackgroundColor: int
        :param BackgroundImageId: 混流-输出流背景图片，取值为实时音视频控制台上传的图片ID。
        :type BackgroundImageId: int
        """
        self.AudioSampleRate = None
        self.AudioBitrate = None
        self.AudioChannels = None
        self.VideoWidth = None
        self.VideoHeight = None
        self.VideoBitrate = None
        self.VideoFramerate = None
        self.VideoGop = None
        self.BackgroundColor = None
        self.BackgroundImageId = None


    def _deserialize(self, params):
        self.AudioSampleRate = params.get("AudioSampleRate")
        self.AudioBitrate = params.get("AudioBitrate")
        self.AudioChannels = params.get("AudioChannels")
        self.VideoWidth = params.get("VideoWidth")
        self.VideoHeight = params.get("VideoHeight")
        self.VideoBitrate = params.get("VideoBitrate")
        self.VideoFramerate = params.get("VideoFramerate")
        self.VideoGop = params.get("VideoGop")
        self.BackgroundColor = params.get("BackgroundColor")
        self.BackgroundImageId = params.get("BackgroundImageId")


class EventList(AbstractModel):
    """sdk或webrtc的事件列表。

    """

    def __init__(self):
        """
        :param Content: 数据内容
        :type Content: list of EventMessage
        :param PeerId: 发送端的userId
        :type PeerId: str
        """
        self.Content = None
        self.PeerId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = EventMessage()
                obj._deserialize(item)
                self.Content.append(obj)
        self.PeerId = params.get("PeerId")


class EventMessage(AbstractModel):
    """事件信息，包括，事件时间戳，事件ID,

    """

    def __init__(self):
        """
        :param Type: 视频流类型：
0：与视频无关的事件；
2：视频为大画面；
3：视频为小画面；
7：视频为旁路画面；
        :type Type: int
        :param Time: 事件上报的时间戳，unix时间（1589891188801ms)
        :type Time: int
        :param EventId: 事件Id：分为sdk的事件和webrtc的事件，详情见：附录/事件 ID 映射表：https://cloud.tencent.com/document/product/647/44916
        :type EventId: int
        :param ParamOne: 事件的第一个参数，如视频分辨率宽
        :type ParamOne: int
        :param ParamTwo: 事件的第二个参数，如视频分辨率高
        :type ParamTwo: int
        """
        self.Type = None
        self.Time = None
        self.EventId = None
        self.ParamOne = None
        self.ParamTwo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Time = params.get("Time")
        self.EventId = params.get("EventId")
        self.ParamOne = params.get("ParamOne")
        self.ParamTwo = params.get("ParamTwo")


class LayoutParams(AbstractModel):
    """MCU混流布局参数

    """

    def __init__(self):
        """
        :param Template: 混流布局模板ID，0为悬浮模板(默认);1为九宫格模板;2为屏幕分享模板;3为画中画模板;4为自定义模板。
        :type Template: int
        :param MainVideoUserId: 屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的用户ID。
        :type MainVideoUserId: str
        :param MainVideoStreamType: 屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的流类型，0为摄像头，1为屏幕分享。左侧大画面为web用户时此值填0。
        :type MainVideoStreamType: int
        :param SmallVideoLayoutParams: 画中画模板中有效，代表小画面的布局参数。
        :type SmallVideoLayoutParams: :class:`tencentcloud.trtc.v20190722.models.SmallVideoLayoutParams`
        :param MainVideoRightAlign: 屏幕分享模板有效。设置为1时代表大画面居右，小画面居左布局。默认为0。
        :type MainVideoRightAlign: int
        :param MixVideoUids: 悬浮模板、九宫格、屏幕分享模板有效。设置此参数后，输出流混合此参数中包含用户的音视频，以及其他用户的纯音频。最多可设置16个用户。
        :type MixVideoUids: list of str
        :param PresetLayoutConfig: 自定义模板中有效，指定用户视频在混合画面中的位置。
        :type PresetLayoutConfig: list of PresetLayoutConfig
        """
        self.Template = None
        self.MainVideoUserId = None
        self.MainVideoStreamType = None
        self.SmallVideoLayoutParams = None
        self.MainVideoRightAlign = None
        self.MixVideoUids = None
        self.PresetLayoutConfig = None


    def _deserialize(self, params):
        self.Template = params.get("Template")
        self.MainVideoUserId = params.get("MainVideoUserId")
        self.MainVideoStreamType = params.get("MainVideoStreamType")
        if params.get("SmallVideoLayoutParams") is not None:
            self.SmallVideoLayoutParams = SmallVideoLayoutParams()
            self.SmallVideoLayoutParams._deserialize(params.get("SmallVideoLayoutParams"))
        self.MainVideoRightAlign = params.get("MainVideoRightAlign")
        self.MixVideoUids = params.get("MixVideoUids")
        if params.get("PresetLayoutConfig") is not None:
            self.PresetLayoutConfig = []
            for item in params.get("PresetLayoutConfig"):
                obj = PresetLayoutConfig()
                obj._deserialize(item)
                self.PresetLayoutConfig.append(obj)


class OneSdkAppIdTranscodeTimeUsagesInfo(AbstractModel):
    """旁路转码时长的查询结果

    """

    def __init__(self):
        """
        :param SdkAppIdTranscodeTimeUsages: 旁路转码时长查询结果数组
        :type SdkAppIdTranscodeTimeUsages: list of SdkAppIdTrtcMcuTranscodeTimeUsage
        :param TotalNum: 查询记录数量
        :type TotalNum: int
        :param SdkAppId: 所查询的应用ID，可能值为:1-应用的应用ID，2-total，显示为total则表示查询的是所有应用的用量合计值。
        :type SdkAppId: str
        """
        self.SdkAppIdTranscodeTimeUsages = None
        self.TotalNum = None
        self.SdkAppId = None


    def _deserialize(self, params):
        if params.get("SdkAppIdTranscodeTimeUsages") is not None:
            self.SdkAppIdTranscodeTimeUsages = []
            for item in params.get("SdkAppIdTranscodeTimeUsages"):
                obj = SdkAppIdTrtcMcuTranscodeTimeUsage()
                obj._deserialize(item)
                self.SdkAppIdTranscodeTimeUsages.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.SdkAppId = params.get("SdkAppId")


class OneSdkAppIdUsagesInfo(AbstractModel):
    """单个SdkAppId的音视频互动计费时长用量数组和数组长度。

    """

    def __init__(self):
        """
        :param TotalNum: 该 SdkAppId 对应的用量记录数长度
        :type TotalNum: int
        :param SdkAppIdTrtcTimeUsages: 用量数组
        :type SdkAppIdTrtcTimeUsages: list of SdkAppIdTrtcUsage
        :param SdkAppId: 应用ID
        :type SdkAppId: str
        """
        self.TotalNum = None
        self.SdkAppIdTrtcTimeUsages = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("SdkAppIdTrtcTimeUsages") is not None:
            self.SdkAppIdTrtcTimeUsages = []
            for item in params.get("SdkAppIdTrtcTimeUsages"):
                obj = SdkAppIdTrtcUsage()
                obj._deserialize(item)
                self.SdkAppIdTrtcTimeUsages.append(obj)
        self.SdkAppId = params.get("SdkAppId")


class OutputParams(AbstractModel):
    """MCU混流的输出参数

    """

    def __init__(self):
        """
        :param StreamId: 直播流 ID，由用户自定义设置，该流 ID 不能与用户旁路的流 ID 相同。
        :type StreamId: str
        :param PureAudioStream: 取值范围[0,1]， 填0：直播流为音视频(默认); 填1：直播流为纯音频
        :type PureAudioStream: int
        :param RecordId: 自定义录制文件名
        :type RecordId: str
        :param RecordAudioOnly: 取值范围[0,1]，填0无实际含义; 填1：指定录制文件格式为mp3
        :type RecordAudioOnly: int
        """
        self.StreamId = None
        self.PureAudioStream = None
        self.RecordId = None
        self.RecordAudioOnly = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.PureAudioStream = params.get("PureAudioStream")
        self.RecordId = params.get("RecordId")
        self.RecordAudioOnly = params.get("RecordAudioOnly")


class PresetLayoutConfig(AbstractModel):
    """自定义模板中有效，指定用户视频在混合画面中的位置。

    """

    def __init__(self):
        """
        :param UserId: 指定显示在该画面上的用户ID。如果不指定用户ID，会按照用户加入房间的顺序自动匹配PresetLayoutConfig中的画面设置。
        :type UserId: str
        :param StreamType: 当该画面指定用户时，代表用户的流类型。0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :type StreamType: int
        :param ImageWidth: 该画面在输出时的宽度，单位为像素值，不填默认为0。
        :type ImageWidth: int
        :param ImageHeight: 该画面在输出时的高度，单位为像素值，不填默认为0。
        :type ImageHeight: int
        :param LocationX: 该画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :type LocationX: int
        :param LocationY: 该画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :type LocationY: int
        :param ZOrder: 该画面在输出时的层级，单位为像素值，不填默认为0。
        :type ZOrder: int
        :param RenderMode: 该画面在输出时的显示模式：0为裁剪，1为缩放，不填默认为0。
        :type RenderMode: int
        """
        self.UserId = None
        self.StreamType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.ZOrder = None
        self.RenderMode = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StreamType = params.get("StreamType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.ZOrder = params.get("ZOrder")
        self.RenderMode = params.get("RenderMode")


class QualityData(AbstractModel):
    """Es返回的质量数据

    """

    def __init__(self):
        """
        :param Content: 数据内容
        :type Content: list of TimeValue
        :param UserId: 用户ID
        :type UserId: str
        :param PeerId: 对端Id,为空时表示上行数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerId: str
        :param DataType: 数据类型
        :type DataType: str
        """
        self.Content = None
        self.UserId = None
        self.PeerId = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.UserId = params.get("UserId")
        self.PeerId = params.get("PeerId")
        self.DataType = params.get("DataType")


class RealtimeData(AbstractModel):
    """查询秒级监控返回的数据

    """

    def __init__(self):
        """
        :param Content: 返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of TimeValue
        :param DataType: 数据类型字段
        :type DataType: str
        """
        self.Content = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.DataType = params.get("DataType")


class RecordUsage(AbstractModel):
    """录制的使用信息。

    """

    def __init__(self):
        """
        :param TimeKey: 本组数据对应的时间点，格式如:2020-09-07或2020-09-07 00:05:05。
        :type TimeKey: str
        :param Class1VideoTime: 视频时长-标清SD，单位：秒。
        :type Class1VideoTime: int
        :param Class2VideoTime: 视频时长-高清HD，单位：秒。
        :type Class2VideoTime: int
        :param Class3VideoTime: 视频时长-超清HD，单位：秒。
        :type Class3VideoTime: int
        :param AudioTime: 语音时长，单位：秒。
        :type AudioTime: int
        """
        self.TimeKey = None
        self.Class1VideoTime = None
        self.Class2VideoTime = None
        self.Class3VideoTime = None
        self.AudioTime = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.Class1VideoTime = params.get("Class1VideoTime")
        self.Class2VideoTime = params.get("Class2VideoTime")
        self.Class3VideoTime = params.get("Class3VideoTime")
        self.AudioTime = params.get("AudioTime")


class RemoveUserByStrRoomIdRequest(AbstractModel):
    """RemoveUserByStrRoomId请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: str
        :param UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")


class RemoveUserByStrRoomIdResponse(AbstractModel):
    """RemoveUserByStrRoomId返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserRequest(AbstractModel):
    """RemoveUser请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        :param UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")


class RemoveUserResponse(AbstractModel):
    """RemoveUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoomState(AbstractModel):
    """房间信息列表

    """

    def __init__(self):
        """
        :param CommId: 通话ID（唯一标识一次通话）
        :type CommId: str
        :param RoomString: 房间号
        :type RoomString: str
        :param CreateTime: 房间创建时间
        :type CreateTime: int
        :param DestroyTime: 房间销毁时间
        :type DestroyTime: int
        :param IsFinished: 房间是否已经结束
        :type IsFinished: bool
        :param UserId: 房间创建者Id
        :type UserId: str
        """
        self.CommId = None
        self.RoomString = None
        self.CreateTime = None
        self.DestroyTime = None
        self.IsFinished = None
        self.UserId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.RoomString = params.get("RoomString")
        self.CreateTime = params.get("CreateTime")
        self.DestroyTime = params.get("DestroyTime")
        self.IsFinished = params.get("IsFinished")
        self.UserId = params.get("UserId")


class ScaleInfomation(AbstractModel):
    """历史规模信息

    """

    def __init__(self):
        """
        :param Time: 每天开始的时间
        :type Time: int
        :param UserNumber: 房间人数，用户重复进入同一个房间为1次
注意：此字段可能返回 null，表示取不到有效值。
        :type UserNumber: int
        :param UserCount: 房间人次，用户每次进入房间为一次
注意：此字段可能返回 null，表示取不到有效值。
        :type UserCount: int
        :param RoomNumbers: sdkappid下一天内的房间数
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomNumbers: int
        """
        self.Time = None
        self.UserNumber = None
        self.UserCount = None
        self.RoomNumbers = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.UserNumber = params.get("UserNumber")
        self.UserCount = params.get("UserCount")
        self.RoomNumbers = params.get("RoomNumbers")


class SdkAppIdRecordUsage(AbstractModel):
    """SdkAppId级别录制时长数据。

    """

    def __init__(self):
        """
        :param SdkAppId: SdkAppId的值。
        :type SdkAppId: str
        :param Usages: 统计的时间点数据。
        :type Usages: list of RecordUsage
        """
        self.SdkAppId = None
        self.Usages = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = RecordUsage()
                obj._deserialize(item)
                self.Usages.append(obj)


class SdkAppIdTrtcMcuTranscodeTimeUsage(AbstractModel):
    """查询旁路转码计费时长。
    查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。

    """

    def __init__(self):
        """
        :param TimeKey: 本组数据对应的时间点，格式如：2020-09-07或2020-09-07 00:05:05。
        :type TimeKey: str
        :param AudioTime: 语音时长，单位：秒。
        :type AudioTime: int
        :param VideoTimeSd: 视频时长-标清SD，单位：秒。
        :type VideoTimeSd: int
        :param VideoTimeHd: 视频时长-高清HD，单位：秒。
        :type VideoTimeHd: int
        :param VideoTimeFhd: 视频时长-全高清FHD，单位：秒。
        :type VideoTimeFhd: int
        """
        self.TimeKey = None
        self.AudioTime = None
        self.VideoTimeSd = None
        self.VideoTimeHd = None
        self.VideoTimeFhd = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.AudioTime = params.get("AudioTime")
        self.VideoTimeSd = params.get("VideoTimeSd")
        self.VideoTimeHd = params.get("VideoTimeHd")
        self.VideoTimeFhd = params.get("VideoTimeFhd")


class SdkAppIdTrtcUsage(AbstractModel):
    """查询音视频互动时长的输出数据。
    查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。

    """

    def __init__(self):
        """
        :param TimeKey: 本组数据对应的时间点，格式如：2020-09-07或2020-09-07 00:05:05。
        :type TimeKey: str
        :param AudioTime: 语音时长，单位：秒。
        :type AudioTime: int
        :param AudioVideoTime: 音视频时长，单位：秒。
2019年10月11日前注册，没有变更为 [新计费模式](https://cloud.tencent.com/document/product/647/17157) 的用户才会返回此值。
        :type AudioVideoTime: int
        :param VideoTimeSd: 视频时长-标清SD，单位：秒。
        :type VideoTimeSd: int
        :param VideoTimeHd: 视频时长-高清HD，单位：秒。
        :type VideoTimeHd: int
        :param VideoTimeHdp: 视频时长-超清HD，单位：秒。
        :type VideoTimeHdp: int
        """
        self.TimeKey = None
        self.AudioTime = None
        self.AudioVideoTime = None
        self.VideoTimeSd = None
        self.VideoTimeHd = None
        self.VideoTimeHdp = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.AudioTime = params.get("AudioTime")
        self.AudioVideoTime = params.get("AudioVideoTime")
        self.VideoTimeSd = params.get("VideoTimeSd")
        self.VideoTimeHd = params.get("VideoTimeHd")
        self.VideoTimeHdp = params.get("VideoTimeHdp")


class SmallVideoLayoutParams(AbstractModel):
    """画中画模板中有效，代表小画面的布局参数

    """

    def __init__(self):
        """
        :param UserId: 代表小画面对应的用户ID。
        :type UserId: str
        :param StreamType: 代表小画面对应的流类型，0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :type StreamType: int
        :param ImageWidth: 小画面在输出时的宽度，单位为像素值，不填默认为0。
        :type ImageWidth: int
        :param ImageHeight: 小画面在输出时的高度，单位为像素值，不填默认为0。
        :type ImageHeight: int
        :param LocationX: 小画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :type LocationX: int
        :param LocationY: 小画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :type LocationY: int
        """
        self.UserId = None
        self.StreamType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StreamType = params.get("StreamType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")


class StartMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    """StartMCUMixTranscodeByStrRoomId请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param StrRoomId: 字符串房间号。
        :type StrRoomId: str
        :param OutputParams: 混流输出控制参数。
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param EncodeParams: 混流输出编码参数。
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param LayoutParams: 混流输出布局参数。
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        """
        self.SdkAppId = None
        self.StrRoomId = None
        self.OutputParams = None
        self.EncodeParams = None
        self.LayoutParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StrRoomId = params.get("StrRoomId")
        if params.get("OutputParams") is not None:
            self.OutputParams = OutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self.EncodeParams = EncodeParams()
            self.EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))


class StartMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    """StartMCUMixTranscodeByStrRoomId返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartMCUMixTranscodeRequest(AbstractModel):
    """StartMCUMixTranscode请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        :param OutputParams: 混流输出控制参数。
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param EncodeParams: 混流输出编码参数。
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param LayoutParams: 混流输出布局参数。
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.OutputParams = None
        self.EncodeParams = None
        self.LayoutParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        if params.get("OutputParams") is not None:
            self.OutputParams = OutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self.EncodeParams = EncodeParams()
            self.EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))


class StartMCUMixTranscodeResponse(AbstractModel):
    """StartMCUMixTranscode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    """StopMCUMixTranscodeByStrRoomId请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param StrRoomId: 字符串房间号。
        :type StrRoomId: str
        """
        self.SdkAppId = None
        self.StrRoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StrRoomId = params.get("StrRoomId")


class StopMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    """StopMCUMixTranscodeByStrRoomId返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMCUMixTranscodeRequest(AbstractModel):
    """StopMCUMixTranscode请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")


class StopMCUMixTranscodeResponse(AbstractModel):
    """StopMCUMixTranscode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TimeValue(AbstractModel):
    """返回的质量数据，时间:值

    """

    def __init__(self):
        """
        :param Time: 时间，unix时间戳（1590065877s)
        :type Time: int
        :param Value: 当前时间返回参数取值，如（bigvCapFps在1590065877取值为0，则Value：0 ）
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class UserInformation(AbstractModel):
    """用户信息，包括用户进房时间，退房时间等

    """

    def __init__(self):
        """
        :param RoomStr: 房间号
        :type RoomStr: str
        :param UserId: 用户Id
        :type UserId: str
        :param JoinTs: 用户进房时间
        :type JoinTs: int
        :param LeaveTs: 用户退房时间，用户没有退房则返回当前时间
        :type LeaveTs: int
        :param DeviceType: 终端类型
        :type DeviceType: str
        :param SdkVersion: Sdk版本号
        :type SdkVersion: str
        :param ClientIp: 客户端IP地址
        :type ClientIp: str
        :param Finished: 判断用户是否已经离开房间
        :type Finished: bool
        """
        self.RoomStr = None
        self.UserId = None
        self.JoinTs = None
        self.LeaveTs = None
        self.DeviceType = None
        self.SdkVersion = None
        self.ClientIp = None
        self.Finished = None


    def _deserialize(self, params):
        self.RoomStr = params.get("RoomStr")
        self.UserId = params.get("UserId")
        self.JoinTs = params.get("JoinTs")
        self.LeaveTs = params.get("LeaveTs")
        self.DeviceType = params.get("DeviceType")
        self.SdkVersion = params.get("SdkVersion")
        self.ClientIp = params.get("ClientIp")
        self.Finished = params.get("Finished")