var obj = JSON.parse($response.body);
var url = $request.url;

switch (true) {
  case url.includes("replyList"):
    obj.data = obj.data.filter((t) => t.id);
    break;
  case url.includes("main/init"):
    obj.data = obj.data.filter((t) => ![944, 945].includes(t.entityId));
    break;
  case url.includes("indexV8"):
    obj.data = obj.data.filter((t) => !["sponsorCard", 8639, 33006].includes(t.entityId) && !t.title.includes("值得买") && !t.title.includes("红包"));
    break;
  case url.includes("dataList"):
    obj.data = obj.data.filter((t) => !("sponsorCard" == t.entityTemplate || t.title.includes("精选配件")));
    break;
  case url.includes("detail"):
    if (obj.data?.hotReplyRows?.length > 0) {
      obj.data.hotReplyRows = obj.data.hotReplyRows.filter((item) => item?.id);
    }
    if (obj.data?.topReplyRows?.length > 0) {
      obj.data.topReplyRows = obj.data.topReplyRows.filter((item) => item?.id);
    }
    const item = ["detailSponsorCard", "include_goods", "include_goods_ids"];
    for (let i of item) {
      if (obj.data?.[i]) {
        obj.data[i] = [];
      }
    }
    break;
  default:
    break;
}
body = JSON.stringify(obj);
$done({ body });
