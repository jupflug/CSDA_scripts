geo_json_geometry = {
  "type": "Polygon",
  "coordinates": [
    [
      [
        -119.05576088657531,
        37.61889954813522
      ],
      [
        -119.07465195862622,
        37.61889954813522
      ],
      [
        -119.07465195862622,
        37.60366497906669
      ],
      [
        -119.05576088657531,
        37.60366497906669
      ],
      [
        -119.05576088657531,
        37.61889954813522
      ]
    ]
  ]
}

# filter for items the overlap with our chosen geometry
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# filter images acquired in a certain date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2019-01-01T00:00:00.000Z",
    "lte": "2019-08-01T00:00:00.000Z"
  }
}

# filter any images which are more than 50% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.05
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
#domain = {
#  "type": "AndFilter",
#  "config": [geometry_filter, date_range_filter]
#}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
domain = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}
