---
title: LBRY的名稱系統如何運作？為什麼不按互聯網域名的方式來分配名稱呢？
category: LBRY 101
order: 4
---

## 問題在於\.\.\.

在談論LBRY中的名稱系統（即URL，統一資源定位系統）如何運作之前，必須先了解以下問題：

**什麼是名稱系統，以及我們為什麼要有一個名稱系統？**

名稱可以將一個人類可以識別並易於理解的單詞或術語映射到一個更難記憶的單詞或術語（比如數字或ID），這是名稱存在的意義。在傳統的DNS（域名系統）中，名稱（即域名）被映射到一個IP地址上。而在LBRY中，名稱被映射到一個唯一的、永久的ID，代表一個數字內容和/或一個創作者的身份。

設計一個高可用性且公平分配名稱的名稱系統是相當困難的。考慮一下你訪問這個文檔（網頁）使用的域名系統。LBRY的域名曾經有很長一段時間是lbry.io，而不是lbry.com。這是因為lbry.com提供了一些獨特的服務嗎? 不！而是因為lbry.com被一個域名搶注者註冊了，而他只想把域名賣給出價最高的人獲利。我們不得不花了好幾個月的時間進行交涉，並支付了一大筆錢，來獲得lbry.com域名的所有權。我們寧願創建一套全新的激勵機制和固定的協議規則，也不希望LBRY用戶也經歷類似事件。

傳統域名系統還有幾個缺陷。它是中心化的，相當於一種審查機制，因為域名持有者並不擁有其域名的真正所有權，真正擁有它們的是域名註冊商。頂級域名（如.io）的任意性很強，邏輯性很弱（如果重新設計域名系統，我們真的想在給定關鍵詞的在極為珍貴的URL後面加上隨便加上一個".com "嗎？再者，LBRY和印度洋 *I*ndian *O*cean有什麼關係嗎？）。最後，域名的固定費用助長了不良行為，也給在域名搶注中出局的人帶來負面影響。

我們希望LBRY的名稱系統擁有如下特點：

- 允許一個單詞直接映射到一個內容上，不需要其他擴展或修飾詞。 
- 允許創作者獲得一個URL，並永久擁有它，而不需要持續付費。 
- 允許一個關鍵詞定位多個內容，同時儘可能保持URL簡短易記。 
- 防止盜用者敲詐創作者。 

在與創作者、消費者、經濟學家、計算機科學家等進行了意義重大的商討後，我們設計了LBRY的名稱系統。

## LBRY名稱系統的工作方式

首先是名稱持有者可以**永久性地獲得一個URL的所有權和控制權。**

在LBRY中，一個URL條目被稱為一個 _認領地址（claim）_。為了簡單起見，一個認領地址可以被認為是由以下部分組成的：

- 名稱(由URL創建者選擇的一串字符) 
- LBRY積分額（LBRY Credits數量）
- 與內容和/或發佈者身份有關的其他數據。 

LBRY中的認領地址是非消耗性的。當你在認領地址中指定了一定的積分額時，除了相對較低的交易費用外，不會破壞或損失其他任何東西。在任何時候，分配給認領地址的LBRY積分都可以被提取出來轉賬到他人，或用於其他目的。當上述情況發生後，此認領地址將失效。

LBRY支持如下幾種類型的名稱解析：

| 名稱類型                 | 解析至                 |
| --------------------- | ----------------------------- | 
| **永久鏈接** <br/> `lbry://<name>#<claim_id>` | 這個URL由一個名稱和隨機分配的ID組成。該名稱由發佈者永久擁有和控制。永久的URL支持部分的、時間順序的ID匹配，所以這些URL可以很短。(比如 lbry://name#8 or lbry://name#ab) |
| **短鏈接** <br/> `lbry://<name>#<short_claim_id>` |這個URL由一個名稱和永久URL中的一個或多個字符（先到先得，以保證唯一性）組成。該名稱由發佈者永久擁有和控制。如果有更短的URL可用，則該更短的URL會取代其解析結果。
| **社區鏈接** <br/> `lbry://<name>` | 在所有名為`<name>`的認領地址中，該地址將解析為含有最多積分投注額的內容。這意味著社區鏈接是由整個社區控制的，而不僅僅是發佈者。這些URL不是永久性的，也並非由社區擁有，而是由社區控制，這允許其被解析到社區認為最合適的內容。 |
| **頻道鏈接** <br/> `lbry://<@channel_name>` | 與發佈者身份對應的URL。將解析到特定發佈者的頻道。頻道URL可以用或不用`#`修飾符來指定。一個不加`#`的URL會返回由社區確定的頻道。
| **內容鏈接** <br/> `lbry://<@channel_name>/<example>` | 將解析至`<@channel_name>`頻道內以`<example>`為名發佈的內容。

## 關鍵信息

1. **名稱不是買來的，而是保留的（reserved）。**這意味著你僅是將積分寄存在了名稱之中。如果你通過競價贏得了一個名稱，你的一些積分將被寄存在該名稱上，直到你決定提取積分為止（只要你願意，任何時候都可）。你並沒有從任何人那裡購買名稱，也沒有人從名稱的轉讓中獲利。這類似於一個測試，測驗誰願意將最多的積分寄存到一個名稱中。這種機制唯一的缺點是，你不能在積分被寄存的時候提取它們或將它們用於其他用途。

2. **社區名稱（社區鏈接）持有的時間越長，其指向就越難更改。** 即使投注了更多的積分，社區控制的URL不會立即改變，而是需要經過一段時間，稱為等待期。名稱每被多控制一個月，就會增加1天的等待期，等待期最多7天（即被控制7個月後，等待期不再延長）。

3. **每個人都有發言權。**如果你認領lbry://bestmovieever，而你的電影質量也不負眾望，那麼用戶的付費將是一股強大力量以保證lbry://bestmovieever持續解析到你的內容。如果社區覺得某個URL的解析不正確，社區成員可以聯合起來進行更改。社區的力量是強大的，它讓不良分子不敢輕舉妄動。這已經被證明是有用的。

4. **名稱如同檢索詞。**當用戶在LBRY網絡上進行搜索或者推送引擎推薦內容時，所有的有效認領地址都會被納入搜索範圍。社區鏈接中找不到你的內容並不意味著你的內容不可見。用戶在網絡上搜索時，可以從同一名稱找到許多不同的內容。

關於名稱認領的更多細節，請參見[claimtrie的實現](https://lbry.tech/spec#claimtrie)。

## 這是一個試驗性功能

無論你是否愛上了這個設計，你很可能會同意，它不同於我們之前所見的任何東西。

最重要的是，LBRY致力於實現真正的內容自由。我們希望為創作者和消費者提供世界上最好的方法，讓他們在沒有中間商的情況下分享數字內容並實現盈利。我們恰恰認為這種方法比其他方法更優越。當然，我們接受反對意見。

我們正試圖以一種新穎的方式解決一個非常困難的問題，我們致力於給這個系統一個機會。目前LBRY網絡上容納了超過100萬條內容，而LBRY名稱系統仍能如願正常運行。不過，一旦我們發現這個系統弊大於利，我們會毫不猶豫地改變它。

## LBRY積分投注額與搜索結果、熱度上升內容、熱門內容的相關性

增加對你內容的LBRY積分投注額，或者你的內容或頻道收到小費，可以提高搜索結果的相關性和你的內容在LBRY的“熱度上升（Trending）”與“熱門（Top）”類別中的曝光度。其中，“熱度提升”類別的內容是基於LBC積分投注額的增加速度快慢計算出來的。[瞭解更多](/faq/trending)。