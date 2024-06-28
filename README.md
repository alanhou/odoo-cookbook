# Odoo 14开发者指南(Cookbook)第四版

内容将逐步搬运至[GitHub开源仓库](https://github.com/iTranslateX)

## 主要内容

[第一章 安装Odoo开发环境](https://github.com/iTranslateX/odoo-cookbook/blob/v14/1.md)：讲解如何为Odoo创建开发环境、启动Odoo、创建配置文件以及启用Odoo开发者工具。

[第二章 管理Odoo服务端实例](https://github.com/iTranslateX/odoo-cookbook/blob/v14/2.md)：提供安装来自GitHub插件的一些有用贴士以及在实例中组织源代码的讲解。

[第三章 创建Odoo插件模块](https://github.com/iTranslateX/odoo-cookbook/blob/v14/3.md)：讲解Odoo插件模块的结构并提供从零开始创建一个简单的Odoo模块的操作指南分解。

[第四章 应用模型](https://github.com/iTranslateX/odoo-cookbook/blob/v14/4.md)：聚焦于Odoo模型结构，并讲解所有字段类型及它们的属性。本章还包含通过继承模块来扩展已有数据库结构的相关技巧。

[第五章 基本服务端开发](https://github.com/iTranslateX/odoo-cookbook/blob/v14/5.md)：讲解Odoo中执行增删改查（CRUD）操作的各类框架方法。本章还包含继承和扩展已有方法的各种方式。

[第六章 管理模块数据](https://github.com/iTranslateX/odoo-cookbook/blob/v14/6.md)：展示如何和模块代码一并进行数据的迁移。还讲解在新发行版中插件修改了数据模型时如何编写迁移脚本。

[第七章 调试模块](https://github.com/iTranslateX/odoo-cookbook/blob/v14/7.md)：提供调试Odoo代码的不同策略并介绍了Python调试器。本章包含在开发者模式下运行Odoo的一些技巧。

[第八章 高级服务端开发技巧](https://github.com/iTranslateX/odoo-cookbook/blob/v14/8.md)：讲解ORM框架更高级的课题。对于开发向导、SQL视图、安装钩子（hook）、on-change方法等非常有用。本章还讲解了如何在数据库中执行原生SQL查询。

[第九章 后端视图](https://github.com/iTranslateX/odoo-cookbook/blob/v14/9.md)：讲解如何为数据模型编写业务视图以及如何在视图中调用服务端方法。涵盖了常用视图(列表、表单和搜索视图)，以及一些更为复杂的视图(看板、图形、日历、透视表等)。

[第十章 权限安全](https://github.com/iTranslateX/odoo-cookbook/blob/v14/10.md/)：讲解如何在Odoo实例中指定谁可以执行什么操作，方式有创建安全组、编写访问控制列表定义在给定模型中每个组可执行的操作，在必要时还可以编写记录级的规则。

[第十一章 国际化](https://github.com/iTranslateX/odoo-cookbook/blob/v14/11.md)：展示Odoo中语言翻译的原理。还讲解如何安装多语言及导入/导出所翻译的词语。

[第十二章 自动化、工作流、Email和打印件](https://github.com/iTranslateX/odoo-cookbook/blob/v14/12.md)：描绘了Odoo中为记录实现业务流程的不同工具。还展示了如何使用服务端动作和自动化规则来对业务规则进行支持。本章还讲解可生成动态PDF文档的QWeb报告。

[第十三章 Web服务端开发](https://github.com/iTranslateX/odoo-cookbook/blob/v14/13.md)：涵盖Odoo web服务端的核心内容。展示了如何创建自定义URL路由来在指定URL上提供数据服务，以及如何对这些URL进行访问控制。

[第十四章 CMS网站开发](https://github.com/iTranslateX/odoo-cookbook/blob/v14/14.md)：讲解如何使用Odoo管理网站。还展示了如何创建和修改美观的网页和QWeb模板。本章还包含如何创建带选项的动态网页构建代码块。它包含一些管理 SEO、用户表单、UTM追踪、网站地图和获取访客地理信息的独立小节。本章还强调了Odoo中最新的多站点概念。

[第十五章 网页客户端开发](https://github.com/iTranslateX/odoo-cookbook/blob/v14/15.md)：深入到Odoo的JavaScript部分。涵盖了如何创建新字段微件以及对服务端发送RPC调用。还包含如何从零开始创建全新的视图。读者还将学习到如何创建操作向导。

[第十六章 Odoo Web Library (OWL)](https://github.com/iTranslateX/odoo-cookbook/blob/v14/16.md)，介绍名为OWL的新客户端框架。涵盖了OWL组件的生命周期。还包含从零创建字段微件的小节。

[第十七章 Odoo的应用内购买](https://github.com/iTranslateX/odoo-cookbook/blob/v14/17.md)：涵盖有关Odoo最新的应用内购买（IAP）概念的所有内容。本章中会学习到如何为IAP创建客户端和服务模块。读者还将学习到如何创建IAP账户并从终端用户提取IAP款项。

[第十八章 自动化测试用例](https://github.com/iTranslateX/odoo-cookbook/blob/v14/18.md)：包含如何编写和执行自动化测试用例。这包括服务端、客户端测试用例。本章还包含导览测试用例以及对失败的测试用例设置headless Chrome来获取视频。

[第十九章 使用Odoo.sh管理、部署和测试](https://github.com/iTranslateX/odoo-cookbook/blob/v14/19.md)：讲解如何通过PaaS平台Odoo.sh来管理、部署和测试Odoo实例。还涉及到如何管理各类实例，如生产、预发布和部署阶段。本章还包含针对Odoo.sh的各种配置选项。

[第二十章 Odoo中的远程过程调用（RPC）](https://github.com/iTranslateX/odoo-cookbook/blob/v14/20.md)：涵盖从外部应用连接Odoo实例的不同方式。本章教你如何通过XML-RPC、JSON-RPC和odoorpc库连接Odoo 以及从Odoo实例访问数据。

[第二十一章 性能优化](https://github.com/iTranslateX/odoo-cookbook/blob/v14/21.md)：讲解用于获取Odoo中性能提升的不同概念和模式。本章包含预提取、ORM缓存和代码性能测试来监测性能问题的概念。

[第二十二章 POS（销售点）](https://github.com/iTranslateX/odoo-cookbook/blob/v14/22.md)：涵盖 POS 应用的自定义。包含对用户界面、添加新动作按钮、修改业务流和扩展客户菜单的自定义。

[第二十三章 在Odoo中管理Email](https://github.com/iTranslateX/odoo-cookbook/blob/v14/23.md)：讲解如何在Odoo中管理email和chatter工具。通过配置邮件服务器开始，然后讲解Odoo框架的邮件API。本章还涵盖Jinja2和QWeb邮件模板、表单视图、字段日志和活动的聊天工具。

[第二十四章 管理IoT盒子](https://github.com/iTranslateX/odoo-cookbook/blob/v14/24.md)：给出了最新的IoT盒子硬件的重点讲解。本章涵盖如何配置、访问和调试IoT盒子。还包含一个集成IoT盒子到你的自定义插件的示范。
