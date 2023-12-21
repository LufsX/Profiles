var requestUrl = $request.url;
var obj = JSON.parse($response.body);

const splashRegex = /^https:\/\/learn\.chaoxing\.com\/apis\/service\/appConfig/;
const bannerRegex = /^https:\/\/home-yd\.chaoxing\.com\/apis\/banner\/getConfigInfoForClient/;

try {
  if (bannerRegex.test(requestUrl)) {
    obj["data"] = [];
  } else if (splashRegex.test(requestUrl)) {
    obj["data"]["ad"] = [];
  }
} catch (e) {
  console.log(e);
}

$done({ body: JSON.stringify(obj) });
