let body = $response.body;
body = JSON.parse(body);
if (body?.response) {
  body.response = body.response || {};
  body.response.user = body.response.user || {};
  body.response.user.is_premium = true;
}
if (body?.user) {
  body.user = body.user || {};
  body.user.is_premium = true;
}
body = JSON.stringify(body);

$done({ body })
// Js by @SukkaW
// https://github.com/SukkaW/Surge/blob/master/Script/pixiv_premium.js