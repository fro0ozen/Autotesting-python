def campaign_data(campaign_name, package_id, url_id, image_id):
    return {"name": campaign_name,
            "objective": "traffic",
            "package_id": package_id,
            "banners": [{
                "urls": {"primary": {"id": url_id}},
                "content": {"image_240x400": {"id": image_id}}
            }]}


def segment_data(segment_name):
    return {"name": f"{segment_name}",
            "pass_condition": 1,
            "relations": [
                {"object_type": "remarketing_player",
                 "params": {"type": "positive",
                            "left": 365,
                            "right": 0}}],
            "logicType": "or"}
