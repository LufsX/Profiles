var obj = JSON.parse($response.body);
var url = $request.url;

switch (true) {
  case url.includes("replyList"):
    obj.data = obj.data.filter((t) => t.id);
    break;
  case url.includes("main/init"):
    obj.data = obj.data.filter((t) => !(945 == t.entityId));
    break;
  case url.includes("indexV8"):
    obj.data = obj.data.filter((t) => !["sponsorCard", 8639, 29349, 33006, 32557].includes(t.entityId) && !t.title.includes("值得买") && !t.title.includes("红包"));
    break;
  case url.includes("dataList"):
    obj.data = obj.data.filter((t) => !("sponsorCard" == t.entityTemplate || t.title.includes("精选配件")));
    break;
  case url.includes("detail"):
    if (obj.data?.hotReplyRows) {
      obj.data.hotReplyRows = obj.data.hotReplyRows.filter((t) => t.id);
    }
    if (obj.data?.topReplyRows) {
      obj.data.topReplyRows = obj.data.topReplyRows.filter((t) => t.id);
    }
    obj.data.include_goods_ids = [];
    obj.data.include_goods = [];
    obj.data.detailSponsorCard = [];
    break;
  default:
    break;
}
body = JSON.stringify(obj);
$done({ body });
