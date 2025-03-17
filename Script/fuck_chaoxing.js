var requestUrl = $request.url;
var obj = JSON.parse($response.body);

// const splashRegex = /^https:\/\/learn\.chaoxing\.com\/apis\/service\/appConfig/;
// const bannerRegex = /^https:\/\/home-yd\.chaoxing\.com\/apis\/banner\/getConfigInfoForClient/;
// const appsRegex = /^https:\/\/apps\.chaoxing\.com\/apis\/recent\/getRecord\.jspx/;

try {
  // if (bannerRegex.test(requestUrl)) {
  //   obj["data"] = [];
  // } else if (splashRegex.test(requestUrl)) {
  //   obj["data"]["ad"] = [];
  // } else if (appsRegex.test(requestUrl)) {
  //   obj["list"] = obj["list"].filter((item) => item.content.resTitle !== "最美图书馆摄影大赛");
  // }
  obj["data"] = [];
} catch (e) {
  console.log(e);
}

$done({ body: JSON.stringify(obj) });
