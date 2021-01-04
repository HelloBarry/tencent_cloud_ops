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


class BlackEmailAddress(AbstractModel):
    """邮箱黑名单结构，包含被拉黑的邮箱地址和被拉黑时间

    """

    def __init__(self):
        """
        :param BounceTime: 邮箱被拉黑时间
        :type BounceTime: str
        :param EmailAddress: 被拉黑的邮箱地址
        :type EmailAddress: str
        """
        self.BounceTime = None
        self.EmailAddress = None


    def _deserialize(self, params):
        self.BounceTime = params.get("BounceTime")
        self.EmailAddress = params.get("EmailAddress")


class CreateEmailAddressRequest(AbstractModel):
    """CreateEmailAddress请求参数结构体

    """

    def __init__(self):
        """
        :param EmailAddress: 您的发信地址，上限为10个
        :type EmailAddress: str
        :param EmailSenderName: 发件人别名
        :type EmailSenderName: str
        """
        self.EmailAddress = None
        self.EmailSenderName = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        self.EmailSenderName = params.get("EmailSenderName")


class CreateEmailAddressResponse(AbstractModel):
    """CreateEmailAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEmailIdentityRequest(AbstractModel):
    """CreateEmailIdentity请求参数结构体

    """

    def __init__(self):
        """
        :param EmailIdentity: 您的发信域名，建议使用三级以上域名。例如：mail.qcloud.com。
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class CreateEmailIdentityResponse(AbstractModel):
    """CreateEmailIdentity返回参数结构体

    """

    def __init__(self):
        """
        :param IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param Attributes: 需要配置的DNS信息
        :type Attributes: list of DNSAttributes
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class CreateEmailTemplateRequest(AbstractModel):
    """CreateEmailTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param TemplateContent: 模板内容
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        self.TemplateName = None
        self.TemplateContent = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))


class CreateEmailTemplateResponse(AbstractModel):
    """CreateEmailTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DNSAttributes(AbstractModel):
    """用于描述DNS记录的域名、记录类型、期望得到的值、目前配置的值

    """

    def __init__(self):
        """
        :param Type: 记录类型 CNAME | A | TXT | MX
        :type Type: str
        :param SendDomain: 域名
        :type SendDomain: str
        :param ExpectedValue: 需要配置的值
        :type ExpectedValue: str
        :param CurrentValue: 腾讯云目前检测到的值
        :type CurrentValue: str
        :param Status: 检测是否通过，创建时默认为false
        :type Status: bool
        """
        self.Type = None
        self.SendDomain = None
        self.ExpectedValue = None
        self.CurrentValue = None
        self.Status = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SendDomain = params.get("SendDomain")
        self.ExpectedValue = params.get("ExpectedValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Status = params.get("Status")


class DeleteBlackListRequest(AbstractModel):
    """DeleteBlackList请求参数结构体

    """

    def __init__(self):
        """
        :param EmailAddressList: 需要清除的黑名单邮箱列表，数组长度至少为1
        :type EmailAddressList: list of str
        """
        self.EmailAddressList = None


    def _deserialize(self, params):
        self.EmailAddressList = params.get("EmailAddressList")


class DeleteBlackListResponse(AbstractModel):
    """DeleteBlackList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailAddressRequest(AbstractModel):
    """DeleteEmailAddress请求参数结构体

    """

    def __init__(self):
        """
        :param EmailAddress: 发信地址
        :type EmailAddress: str
        """
        self.EmailAddress = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")


class DeleteEmailAddressResponse(AbstractModel):
    """DeleteEmailAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailIdentityRequest(AbstractModel):
    """DeleteEmailIdentity请求参数结构体

    """

    def __init__(self):
        """
        :param EmailIdentity: 发信域名
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class DeleteEmailIdentityResponse(AbstractModel):
    """DeleteEmailIdentity返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailTemplateRequest(AbstractModel):
    """DeleteEmailTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateID: 删除发信模版
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")


class DeleteEmailTemplateResponse(AbstractModel):
    """DeleteEmailTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EmailIdentity(AbstractModel):
    """发信域名验证列表结构体

    """

    def __init__(self):
        """
        :param IdentityName: 发信域名
        :type IdentityName: str
        :param IdentityType: 验证类型，固定为DOMAIN
        :type IdentityType: str
        :param SendingEnabled: 是否已通过验证
        :type SendingEnabled: bool
        """
        self.IdentityName = None
        self.IdentityType = None
        self.SendingEnabled = None


    def _deserialize(self, params):
        self.IdentityName = params.get("IdentityName")
        self.IdentityType = params.get("IdentityType")
        self.SendingEnabled = params.get("SendingEnabled")


class EmailSender(AbstractModel):
    """用于描述发件人相关信息

    """

    def __init__(self):
        """
        :param EmailAddress: 发信地址
        :type EmailAddress: str
        :param EmailSenderName: 发信人别名
注意：此字段可能返回 null，表示取不到有效值。
        :type EmailSenderName: str
        :param CreatedTimestamp: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTimestamp: int
        """
        self.EmailAddress = None
        self.EmailSenderName = None
        self.CreatedTimestamp = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        self.EmailSenderName = params.get("EmailSenderName")
        self.CreatedTimestamp = params.get("CreatedTimestamp")


class GetEmailIdentityRequest(AbstractModel):
    """GetEmailIdentity请求参数结构体

    """

    def __init__(self):
        """
        :param EmailIdentity: 发信域名
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class GetEmailIdentityResponse(AbstractModel):
    """GetEmailIdentity返回参数结构体

    """

    def __init__(self):
        """
        :param IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param Attributes: DNS配置详情
        :type Attributes: list of DNSAttributes
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class GetEmailTemplateRequest(AbstractModel):
    """GetEmailTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateID: 模板ID
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")


class GetEmailTemplateResponse(AbstractModel):
    """GetEmailTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateContent: 模板内容数据
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateContent = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        self.RequestId = params.get("RequestId")


class GetStatisticsReportRequest(AbstractModel):
    """GetStatisticsReport请求参数结构体

    """

    def __init__(self):
        """
        :param StartDate: 开始日期
        :type StartDate: str
        :param EndDate: 结束日期
        :type EndDate: str
        :param Domain: 发信域名
        :type Domain: str
        :param ReceivingMailboxType: 收件方邮箱类型，例如gmail.com
        :type ReceivingMailboxType: str
        """
        self.StartDate = None
        self.EndDate = None
        self.Domain = None
        self.ReceivingMailboxType = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Domain = params.get("Domain")
        self.ReceivingMailboxType = params.get("ReceivingMailboxType")


class GetStatisticsReportResponse(AbstractModel):
    """GetStatisticsReport返回参数结构体

    """

    def __init__(self):
        """
        :param DailyVolumes: 发信统计报告，按天
        :type DailyVolumes: list of Volume
        :param OverallVolume: 发信统计报告，总览
        :type OverallVolume: :class:`tencentcloud.ses.v20201002.models.Volume`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DailyVolumes = None
        self.OverallVolume = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DailyVolumes") is not None:
            self.DailyVolumes = []
            for item in params.get("DailyVolumes"):
                obj = Volume()
                obj._deserialize(item)
                self.DailyVolumes.append(obj)
        if params.get("OverallVolume") is not None:
            self.OverallVolume = Volume()
            self.OverallVolume._deserialize(params.get("OverallVolume"))
        self.RequestId = params.get("RequestId")


class ListBlackEmailAddressRequest(AbstractModel):
    """ListBlackEmailAddress请求参数结构体

    """

    def __init__(self):
        """
        :param StartDate: 开始日期
        :type StartDate: str
        :param EndDate: 结束日期
        :type EndDate: str
        :param Limit: 规范，配合Offset使用
        :type Limit: int
        :param Offset: 规范，配合Limit使用
        :type Offset: int
        :param EmailAddress: 可以指定邮箱进行查询
        :type EmailAddress: str
        :param TaskID: 可以指定任务ID进行查询
        :type TaskID: str
        """
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Offset = None
        self.EmailAddress = None
        self.TaskID = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.EmailAddress = params.get("EmailAddress")
        self.TaskID = params.get("TaskID")


class ListBlackEmailAddressResponse(AbstractModel):
    """ListBlackEmailAddress返回参数结构体

    """

    def __init__(self):
        """
        :param BlackList: 黑名单列表
        :type BlackList: list of BlackEmailAddress
        :param TotalCount: 黑名单总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlackList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BlackList") is not None:
            self.BlackList = []
            for item in params.get("BlackList"):
                obj = BlackEmailAddress()
                obj._deserialize(item)
                self.BlackList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListEmailAddressRequest(AbstractModel):
    """ListEmailAddress请求参数结构体

    """


class ListEmailAddressResponse(AbstractModel):
    """ListEmailAddress返回参数结构体

    """

    def __init__(self):
        """
        :param EmailSenders: 发信地址列表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type EmailSenders: list of EmailSender
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EmailSenders = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailSenders") is not None:
            self.EmailSenders = []
            for item in params.get("EmailSenders"):
                obj = EmailSender()
                obj._deserialize(item)
                self.EmailSenders.append(obj)
        self.RequestId = params.get("RequestId")


class ListEmailIdentitiesRequest(AbstractModel):
    """ListEmailIdentities请求参数结构体

    """


class ListEmailIdentitiesResponse(AbstractModel):
    """ListEmailIdentities返回参数结构体

    """

    def __init__(self):
        """
        :param EmailIdentities: 发信域名列表
        :type EmailIdentities: list of EmailIdentity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EmailIdentities = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailIdentities") is not None:
            self.EmailIdentities = []
            for item in params.get("EmailIdentities"):
                obj = EmailIdentity()
                obj._deserialize(item)
                self.EmailIdentities.append(obj)
        self.RequestId = params.get("RequestId")


class ListEmailTemplatesRequest(AbstractModel):
    """ListEmailTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 获取模版数据量，用于分页
        :type Limit: int
        :param Offset: 获取模版偏移值，用于分页
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class ListEmailTemplatesResponse(AbstractModel):
    """ListEmailTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TemplatesMetadata: 邮件模板列表
        :type TemplatesMetadata: list of TemplatesMetadata
        :param TotalCount: 模版总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplatesMetadata = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplatesMetadata") is not None:
            self.TemplatesMetadata = []
            for item in params.get("TemplatesMetadata"):
                obj = TemplatesMetadata()
                obj._deserialize(item)
                self.TemplatesMetadata.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class SendEmailRequest(AbstractModel):
    """SendEmail请求参数结构体

    """

    def __init__(self):
        """
        :param FromEmailAddress: 发信邮件地址。例如：noreply@mail.qcloud.com。
        :type FromEmailAddress: str
        :param Destination: 收信人邮箱地址
        :type Destination: list of str
        :param Subject: 邮件主题
        :type Subject: str
        :param ReplyToAddresses: 邮件的“回复”电子邮件地址。可以填写您能收到邮件的邮箱地址，可以是个人邮箱。如果不填，收件人将会回复到腾讯云。
        :type ReplyToAddresses: str
        :param Template: 使用模板发送时，填写的模板相关参数
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param Simple: 使用API直接发送内容时，填写的邮件内容
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        """
        self.FromEmailAddress = None
        self.Destination = None
        self.Subject = None
        self.ReplyToAddresses = None
        self.Template = None
        self.Simple = None


    def _deserialize(self, params):
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.Destination = params.get("Destination")
        self.Subject = params.get("Subject")
        self.ReplyToAddresses = params.get("ReplyToAddresses")
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self.Simple = Simple()
            self.Simple._deserialize(params.get("Simple"))


class SendEmailResponse(AbstractModel):
    """SendEmail返回参数结构体

    """

    def __init__(self):
        """
        :param MessageId: 接受消息时生成的消息的唯一标识符。
        :type MessageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MessageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.RequestId = params.get("RequestId")


class Simple(AbstractModel):
    """邮件发送的内容，可以是纯文本(TEXT)，也可以是纯代码(HTML)，或者纯文本+HTML的组合(建议方式)

    """

    def __init__(self):
        """
        :param Html: base64之后的Html代码。需要包含所有的代码信息，不要包含外部css，否则会导致显示格式错乱
        :type Html: str
        :param Text: base64之后的纯文本信息，如果没有Html，邮件中会直接显示纯文本；如果有Html，它代表邮件的纯文本样式
        :type Text: str
        """
        self.Html = None
        self.Text = None


    def _deserialize(self, params):
        self.Html = params.get("Html")
        self.Text = params.get("Text")


class Template(AbstractModel):
    """模板发送相关信息，包含模板ID，模板变量参数等信息

    """

    def __init__(self):
        """
        :param TemplateID: 模板ID。如果没有模板，请先新建一个
        :type TemplateID: int
        :param TemplateData: 模板中的变量参数，请使用json.dump将json对象格式化为string类型。该对象是一组键值对，每个Key代表模板中的一个变量，模板中的变量使用{{键}}表示，相应的值在发送时会被替换为{{值}}。
        :type TemplateData: str
        """
        self.TemplateID = None
        self.TemplateData = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        self.TemplateData = params.get("TemplateData")


class TemplateContent(AbstractModel):
    """模板内容，TEXT和HTML必须至少存在一项，建议使用TEXT和HTML的组合

    """

    def __init__(self):
        """
        :param Html: base64之后的Html代码
        :type Html: str
        :param Text: base64之后的文本内容
        :type Text: str
        """
        self.Html = None
        self.Text = None


    def _deserialize(self, params):
        self.Html = params.get("Html")
        self.Text = params.get("Text")


class TemplatesMetadata(AbstractModel):
    """模板列表结构

    """

    def __init__(self):
        """
        :param CreatedTimestamp: 创建时间
        :type CreatedTimestamp: int
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param TemplateStatus: 模板状态。1-审核中|0-已通过|2-拒绝|其它-不可用
        :type TemplateStatus: int
        :param TemplateID: 模板ID
        :type TemplateID: int
        :param ReviewReason: 审核原因
        :type ReviewReason: str
        """
        self.CreatedTimestamp = None
        self.TemplateName = None
        self.TemplateStatus = None
        self.TemplateID = None
        self.ReviewReason = None


    def _deserialize(self, params):
        self.CreatedTimestamp = params.get("CreatedTimestamp")
        self.TemplateName = params.get("TemplateName")
        self.TemplateStatus = params.get("TemplateStatus")
        self.TemplateID = params.get("TemplateID")
        self.ReviewReason = params.get("ReviewReason")


class UpdateEmailIdentityRequest(AbstractModel):
    """UpdateEmailIdentity请求参数结构体

    """

    def __init__(self):
        """
        :param EmailIdentity: 请求验证的域名
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class UpdateEmailIdentityResponse(AbstractModel):
    """UpdateEmailIdentity返回参数结构体

    """

    def __init__(self):
        """
        :param IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param Attributes: 需要配置的DNS信息
        :type Attributes: list of DNSAttributes
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class UpdateEmailTemplateRequest(AbstractModel):
    """UpdateEmailTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateContent: 模板内容
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param TemplateID: 模板ID
        :type TemplateID: int
        :param TemplateName: 模版名字
        :type TemplateName: str
        """
        self.TemplateContent = None
        self.TemplateID = None
        self.TemplateName = None


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        self.TemplateID = params.get("TemplateID")
        self.TemplateName = params.get("TemplateName")


class UpdateEmailTemplateResponse(AbstractModel):
    """UpdateEmailTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Volume(AbstractModel):
    """统计数据的结构体

    """

    def __init__(self):
        """
        :param SendDate: 日期
注意：此字段可能返回 null，表示取不到有效值。
        :type SendDate: str
        :param RequestCount: 邮件请求数量
        :type RequestCount: int
        :param AcceptedCount: 腾讯云通过数量
        :type AcceptedCount: int
        :param DeliveredCount: 送达数量
        :type DeliveredCount: int
        :param OpenedCount: 打开邮件的用户数量，根据收件人去重
        :type OpenedCount: int
        :param ClickedCount: 点击了邮件中的链接数量用户数量
        :type ClickedCount: int
        :param BounceCount: 退信数量
        :type BounceCount: int
        :param UnsubscribeCount: 取消订阅的用户数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnsubscribeCount: int
        """
        self.SendDate = None
        self.RequestCount = None
        self.AcceptedCount = None
        self.DeliveredCount = None
        self.OpenedCount = None
        self.ClickedCount = None
        self.BounceCount = None
        self.UnsubscribeCount = None


    def _deserialize(self, params):
        self.SendDate = params.get("SendDate")
        self.RequestCount = params.get("RequestCount")
        self.AcceptedCount = params.get("AcceptedCount")
        self.DeliveredCount = params.get("DeliveredCount")
        self.OpenedCount = params.get("OpenedCount")
        self.ClickedCount = params.get("ClickedCount")
        self.BounceCount = params.get("BounceCount")
        self.UnsubscribeCount = params.get("UnsubscribeCount")