let obj = JSON.parse($response.body);
obj.result["xy_svip_expire"] = 4102415999;
obj.result["svip_expired_at"] = 4102415999;
obj.result["is_xy_vip"] = true;
obj.result["is_vip"] = true;
obj.result["vip_type"] = "s";
$done({ body: JSON.stringify(obj) });
