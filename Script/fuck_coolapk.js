var requestUrl = $request.url;
var body = $response.body;
var obj = JSON.parse(body);

const replyListRegex = /^https:\/\/api\.coolapk\.com\/v6\/feed\/replyList/;
const detailRegex = /^https:\/\/api\.coolapk\.com\/v6\/feed\/detail/;
const indexRegex = /^https:\/\/api\.coolapk\.com\/v6\/main\/indexV8/;
const dataListRegex = /^https:\/\/api\.coolapk\.com\/v6\/page\/dataList/;
const loadConfigRegex = /^https:\/\/api\.coolapk\.com\/v6\/account\/loadConfig/;
const initRegex = /^https:\/\/api\.coolapk\.com\/v6\/main\/init/;
const jdItemRegex = /item\.m\.jd/;
const startupPageRegex = /启动页/;

try {
  if (replyListRegex.test(requestUrl)) {
    obj.data = obj.data.filter((item) => item.id);
  } else if (detailRegex.test(requestUrl)) {
    clearDetailFields(obj.data);
  } else if (indexRegex.test(requestUrl)) {
    obj.data = obj.data.filter((item) => filterIndexData(item));
  } else if (dataListRegex.test(requestUrl)) {
    obj.data.forEach((el) => clearDetailFields(el));
  } else if (loadConfigRegex.test(requestUrl)) {
    obj.data[0].entities = [];
  } else if (initRegex.test(requestUrl)) {
    optimizeInitData(obj.data);
  }
} catch (e) {
  console.log(e);
}

body = JSON.stringify(obj);
$done({ body });

function clearDetailFields(data) {
  data.include_goods = [];
  data.detailSponsorCard = [];
  data.extra_title = "";
  data.extra_pic = "";
  data.extra_key = "";
  data.extra_type = "";
  data.extra_url = "";
  data.extra_info = "";
  data.extra_entities = [];
  data.extra_fromApi = "";
  delete data.goodsListInfo;
}

function filterIndexData(item) {
  if (item.entityTemplate === "imageCarouselCard_1" && item.entities) {
    item.entities = item.entities.filter((el) => (el.title !== "jd" && el.title.includes("今日酷安")) || el.title.includes("众测"));
  } else if (item.entityTemplate === "listCard") {
    return false;
  } else if (item.extra_title !== "") {
    clearDetailFields(item);
  }
  return true;
}

function optimizeInitData(data) {
  const filteredList = data.filter((el) => el.url.indexOf("item.m.jd") === -1 || el.title.indexOf("启动页") === -1);
  filteredList.forEach((el) => {
    if (el.entityTemplate === "configCard") {
      const objTem = { cardId: el.extraDataArr.cardId, cardPageName: el.extraDataArr.cardPageName, selectedHomeTab: el.extraDataArr.selectedHomeTab };
      el.extraDataArr = objTem;
      el.extraData = JSON.stringify(objTem);
    }
  });
  data = filteredList;
}
