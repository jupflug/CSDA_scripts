geo_json_geometry = {
  "type": "Polygon",
  "coordinates": [
    [
      [
        -119.74493441554253,
        37.7876815499704
      ],
      [
        -119.74493441554253,
        37.76670385983432
      ],
      [
        -119.722746102245,
        37.76670385983432
      ],
      [
        -119.722746102245,
        37.7876815499704
      ],
      [
        -119.74493441554253,
        37.7876815499704
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
    "gte": "2017-01-01T00:00:00.000Z",
    "lte": "2017-07-01T00:00:00.000Z"
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
