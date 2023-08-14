var requestUrl = $request.url;
var body = $response.body;
var obj = JSON.parse(body);

try {
  if (/^https:\/\/api\.coolapk\.com\/v6\/feed\/replyList/.test(requestUrl)) {
    obj.data = obj.data.filter((item) => item.id);
  } else if (/^https:\/\/api\.coolapk\.com\/v6\/feed\/detail/.test(requestUrl)) {
    obj.data.include_goods = [];
    obj.data.detailSponsorCard = [];
    obj.data.extra_title = "";
    obj.data.extra_pic = "";
    obj.data.extra_key = "";
    obj.data.extra_type = "";
    obj.data.extra_url = "";
    obj.data.extra_info = "";
    obj.data.extra_fromApi = "";
    delete obj.data.goodsListInfo;
    obj.data.extra_entities = [];
  } else if (/^https:\/\/api\.coolapk\.com\/v6\/main\/indexV8/.test(requestUrl)) {
    obj.data = obj.data.filter((item) => {
      if (item.entityTemplate === "imageCarouselCard_1" && item.entities) {
        item.entities = item.entities.filter((el) => (el.title !== "jd" && el.title.includes("今日酷安")) || el.title.includes("众测"));
      } else if (item.entityTemplate === "listCard") {
        return false;
      } else if (item.extra_title !== "") {
        item.extra_title = "";
        item.extra_pic = "";
        item.extra_key = "";
        item.extra_type = "";
        item.extra_url = "";
        item.extra_info = "";
        item.extra_entities = [];
        item.extra_fromApi = "";
        delete item.goodsListInfo;
      }
      return true;
    });
  } else if (/^https:\/\/api\.coolapk\.com\/v6\/page\/dataList/.test(requestUrl)) {
    obj.data.forEach((el) => {
      el.extra_title = "";
      el.extra_pic = "";
      el.extra_key = "";
      el.extra_type = "";
      el.extra_url = "";
      el.extra_info = "";
      el.extra_entities = [];
      el.extra_fromApi = "";
      delete el.goodsListInfo;
    });
  } else if (/^https:\/\/api\.coolapk\.com\/v6\/account\/loadConfig/.test(requestUrl)) {
    obj.data[0].entities = [];
  } else if (/^https:\/\/api\.coolapk\.com\/v6\/main\/init/.test(requestUrl)) {
    let list = obj.data.filter((el) => el.url.indexOf("item.m.jd") === -1 || el.title.indexOf("启动页") === -1);
    list.forEach((el) => {
      if (el.entityTemplate === "configCard") {
        let objTem = { cardId: el.extraDataArr.cardId, cardPageName: el.extraDataArr.cardPageName, selectedHomeTab: el.extraDataArr.selectedHomeTab };
        el.extraDataArr = objTem;
        el.extraData = JSON.stringify(objTem);
      }
    });
    obj.data = list;
  }
} catch (e) {
  console.log(e);
}

body = JSON.stringify(obj);
$done({ body });
