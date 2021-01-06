---
title: How does LBRY naming work? Why don't you just assign names the same way as internet domains?
category: LBRY 101
order: 4
---

## The problem

Before talking about how names (URLs) in LBRY work, it's important to understand the problem. What is a naming system and why do we have one?

Names exist so that we can map a human-readable and understandable word or term to a more difficult one to remember like number or ID. In the traditional DNS (domain name system), names are mapped to a numerical IP address. In LBRY, names are mapped to a unique, permanent ID representing a piece of digital content and/or a publisher identity.

Designing a naming system that works well and fairly assigns names is quite hard! Consider the domain system you are likely using to access this document. LBRY's domain used to be lbry.io for a long time, rather than lbry.com. Is it because lbry.com is providing some unique service? No! It is because a squatter was in possession of it, simply looking to auction the domain name to the highest bidder in demand. We had to negotiate for months (and pay lots of $$$) to get in possession of the lbry.com domain and we don't want LBRY users to go through a similar experience...we'd rather leave it up to incentives and fixed protocol rules.  

The traditional system has several other flaws. It is centralized and a mechanism of censorship, as holders do not have true ownership of their domain, only the top-level provider. Top-level domains (like .io) are also arbitrary and largely illogical (if designing the domain name system again, would we really want to add an arbitrary ".com" to the most prestigious URL for a given keyword? does LBRY have anything to do with the *I*ndian *O*cean?). Finally, in addition to incentivizing bad behavior, the flat-fee structure of domains prevents the good behavior from those who are priced out.

We wanted a system that:

- Allows a single word to be mapped directly to a piece of content, with no other extension or modifier.
- Allows creators to acquire a URL and own it permanently and forever, without ongoing fees.
- Allows multiple pieces of content to be located at a single keyword while keeping URLs as short and memorable as possible.
- Prevents squatters from extorting creators.

After meaningful consultation with creators, consumers, economists, computer scientists, and more, we devised LBRY's naming system.

## How LBRY Does Naming

First and foremost **it is absolutely possible to own and control a URL forever**.

In LBRY, a URL entry is called a _claim_. For simplicity, a claim can be considered to consist of:

- The name (a string of characters chosen by the creator)
- The number of credits
- Additional data related to the content and/or publisher identity

Claims in LBRY are non-consumptive. When you designate a number of credits in a claim, nothing is lost or destroyed beyond the relatively minimal transaction fee. At any time, the credits allocated to a claim can be used for another purpose, recovered, or sent somewhere else. When this happens, the claim is no longer considered valid.

LBRY supports several types of URL resolution:

| Type                 | Resolution                 |
| --------------------- | ----------------------------- | -------------------------- |
| **Permanent** <br/> `lbry://<name>#<claim_id>` | This URL consists of a name and randomly assigned ID. This is permanently owned and controlled by the publisher. Permanent URLs support partial, temporal-ordered ID matching, so these can be quite short (e.g. lbry://name#8 or lbry://name#ab) |
| **Short** <br/> `lbry://<name>#<short_claim_id>` | This URL consists of a name and one or more characters (first come first serve to preserve uniqueness) from the Permanent URL. This is permanently owned and controlled by the publisher. If a shorter URL is made available, the claim next in line will take over its resolution.
| **Community** <br/> `lbry://<name>` | Of all of the claims named `<name>`, this returns the publish with the most credits committed towards it, not just by the publisher, but by the entire community. These URLs are not permanent or owned but instead controlled by the community itself, allowing the resolution to settle on that which the community determines most appropriate. |
| **Channel** <br/> `lbry://<@channel_name>` | A URL corresponding to a publisher identity. These resolve to the identity of a specific publisher and their publishes. Channel URLs can be specified with or without the `#` modifier. An unmodified URL returns the channel determined by the community.
| **Signed** <br/> `lbry://<@channel_name>/<example>` | The piece of content published to the name `<example>` within the channel of `<@channel_name>`.

## Takeaways

1. **Names aren't bought, only reserved – no credits are lost, only put on deposit.** If you win the auction for a name, your credits are held with that name until you decide to withdraw them (at any time you wish). You aren't buying the name from anyone, and no one profits off of the transfer of names. It's just a test of who is willing to deposit the most credits toward a name. The only downside is that you can't spend the credits on content or withdraw them while they are in reserve.

2. **The longer a community name is held, the longer it sticks.** Community-controlled URLs don't change instantly if more credits are designated – especially if you've held it for a while. For every month a name is controlled, 1 day is added to the waiting period, for a maximum of 7 days (after 7 months).

3. **Everyone has a say.** If you claim lbry://bestmovieever and your film lives up to the hype, user tips and purchases are a strong force keeping your content there. If the community feels a URL resolution is incorrect, they can band together to change it anytime. This is a powerful force keeping bad actors at bay that has already proved useful.

4. **Names are more like search terms.** When a user searches the LBRY network, or a recommendation engine suggests content, all valid claims are considered. Not having the community URL for your content does not mean no one will see it. Many different pieces of content under the same name can be displayed when users look for content on the network.

For more details on claims, please see the [claimtrie implementation](https://lbry.tech/spec#claimtrie)

## Experimentation

Whether you're in love with this design or not, you'd likely agree it's unlike anything we've seen before.

The bottom line is that LBRY is dedicated to providing true content freedom. We want to provide the world's best method for creators and consumers to share and monetize digital content without intermediaries. We happen to think this is a superior method to the alternatives, but we're also not dogmatic about it.

We're trying to solve a very hard problem in a novel way, and we're committed to giving this system a chance. 1,000,000 pieces of content in, it has worked seamlessly. But if we ever saw this system harming rather than helping, we wouldn't hesitate to change it.

## Relevance in search and trending/top categories

Increasing your bid and receiving tips on your content/channel, increases its relevance in search results and discoverability through the Trending and Top categories on LBRY. Trending calculations are based on how much the LBC bid has increased through any bid updates and tips, compared to all the other claims on LBRY. [Learn more](/faq/trending).


问题
在谈论LBRY中的名称（URL）如何工作之前，必须先了解这个问题。什么是命名系统，为什么我们要有一个命名系统？

名字的存在是为了让我们可以将一个人类可读可理解的单词或术语映射到一个更难记忆的单词或术语，比如数字或ID。在传统的DNS（域名系统）中，名字被映射到一个数字IP地址上。在LBRY中，名称被映射到一个独特的、永久的ID，代表一个数字内容和/或一个出版商的身份。

设计一个好用且公平分配名称的命名系统是相当困难的! 考虑一下你可能使用的域名系统来访问这个文档。LBRY的域名曾经有很长一段时间是lbry.io，而不是lbry.com。是因为lbry.com提供了一些独特的服务吗? 不！不是的。是因为有一个寮房拥有它，只是想把域名拍卖给需求量最大的出价者。我们不得不花了好几个月的时间进行谈判（并支付了大量的美元）来获得lbry.com域名的所有权，我们不希望LBRY用户也经历类似的经历......我们宁愿把它留给激励机制和固定的协议规则。

传统的系统还有几个缺陷。它是中心化的，也是一种审查机制，因为持有者并不拥有其域名的真正所有权，只有顶层提供者才拥有。顶级域名(如.io)也是任意的，而且基本上不符合逻辑(如果重新设计域名系统，我们真的想在给定关键词的最负盛名的网址上加上一个任意的".com "吗?LBRY和印度洋有什么关系吗?)。最后，除了激励不良行为外，域名的统一收费结构还阻止了那些被定价的良好行为。

我们想要的系统是

允许一个词直接映射到一个内容上，不需要其他扩展或修饰词。
允许创作者获得一个URL，并永久拥有它，而不需要持续的费用。
允许一个关键词定位多个内容，同时尽可能保持URL的简短和易记。
防止盗用者敲诈创作者。
在与创作者、消费者、经济学家、计算机科学家等进行了有意义的咨询后，我们设计了LBRY的命名系统。

LBRY如何进行命名
首先是绝对可以永远拥有和控制一个URL。

在LBRY中，一个URL条目被称为一个权利要求。为了简单起见，一个权利要求可以被认为是由以下部分组成的。

名称(由创建者选择的一串字符)
学分数量
与内容和/或出版商身份有关的其他数据。
LBRY中的债权是非消耗性的。当您在债权中指定了一定数量的信用点时，除了相对较低的交易费用外，没有任何东西会被丢失或破坏。在任何时候，分配给索赔的信用额度都可以被用于另一个目的，恢复，或被发送到其他地方。当这种情况发生时，债权就不再被认为是有效的。

LBRY支持几种类型的URL解析。

经验教训
名字不是买来的，而是保留的--没有信用点的损失，只有存款。如果您在拍卖会上赢得了一个名字，您的信用点将被保留在该名字上，直到您决定提取信用点为止（在您愿意的任何时候）。您并没有从任何人那里购买名字，也没有人从名字的转让中获利。这只是一个测试，看谁愿意将最多的信用点数存入一个名字。唯一的缺点是，你不能将信用点用于内容，也不能在信用点被保留的时候提取它们。

社区名称持有的时间越长，坚持的时间就越长。如果指定了更多的信用点，社区控制的URL不会立即改变--尤其是当你持有一段时间后。名字每被控制一个月，就会增加1天的等待期，最多7天（7个月后）。

每个人都有发言权。如果你宣称lbry://bestmovieever，而你的电影也不负众望，用户的提示和购买是保持你的内容的强大力量。如果社区觉得某个URL分辨率不正确，他们可以联合起来随时更改。这是一股强大的力量，让不良分子不敢轻举妄动，这已经被证明是有用的。

名字更像是搜索词。当用户搜索LBRY网络，或者推荐引擎推荐内容时，所有的有效诉求都会被考虑。没有你的内容的社区网址，并不意味着没有人会看到它。当用户在网络上查找内容时，可以在同一名称下显示许多不同的内容。

关于诉求的更多细节，请看claimtrie的实现。

实验
无论你是否爱上了这个设计，你很可能会同意它不同于我们之前看到的任何东西。

底线是，LBRY致力于提供真正的内容自由。我们希望为创作者和消费者提供世界上最好的方法，让他们在没有中间商的情况下分享数字内容并实现盈利。我们恰好认为这是一种比其他方法更优越的方法，但我们也不是教条主义。

我们正试图以一种新颖的方式解决一个非常困难的问题，我们致力于给这个系统一个机会。100万条内容进去，它已经无缝地工作了。但如果我们曾经看到这个系统有伤害而不是帮助，我们会毫不犹豫地改变它。

搜索和趋势/顶级类别的相关性
增加你的出价并收到关于你的内容/频道的提示，通过LBRY上的 "趋势 "和 "热门 "类别增加其在搜索结果中的相关性和可发现性。趋势计算是基于LBC出价通过任何出价更新和提示增加了多少，与LBRY上的所有其他声明相比。了解更多信息。
