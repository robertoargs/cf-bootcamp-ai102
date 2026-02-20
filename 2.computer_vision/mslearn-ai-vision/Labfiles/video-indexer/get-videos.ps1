$account_id="aa2b02da-76ac-4129-8dd3-dd6f9f3eed07"
$api_key="6b31134cc45843e6a23905ff83c1cb76"
$location="trial"

# Clear the console window
cls

# Call the AccessToken method with the API key in the header to get an access token
$token = Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/auth/$location/Accounts/$account_id/AccessToken" -Headers @{'Ocp-Apim-Subscription-Key' = $api_key}

# Use the access token to make an authenticated call to the Videos method to get a list of videos in the account
Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/$location/Accounts/$account_id/Videos?accessToken=$token" | ConvertTo-Json -Depth 6

# {
#     "results":  [
#                     {
#                         "accountId":  "aa2b02da-76ac-4129-8dd3-dd6f9f3eed07",
#                         "id":  "l7hpcdtybs",
#                         "partition":  null,
#                         "externalId":  null,
#                         "metadata":  null,
#                         "name":  "Responsible AI",
#                         "description":  null,
#                         "created":  "2026-02-20T22:09:15.9966667+00:00",
#                         "lastModified":  "2026-02-20T22:11:15.54+00:00",
#                         "lastIndexed":  "2026-02-20T22:11:15.54+00:00",
#                         "privacyMode":  "Private",
#                         "userName":  "Roberto Gutierrez",
#                         "isOwned":  true,
#                         "isBase":  true,
#                         "hasSourceVideoFile":  true,
#                         "state":  "Processed",
#                         "moderationState":  "OK",
#                         "reviewState":  "None",
#                         "isSearchable":  true,
#                         "processingProgress":  "100%",
#                         "durationInSeconds":  114,
#                         "thumbnailVideoId":  "l7hpcdtybs",
#                         "thumbnailId":  "7c76b4a4-f35b-4c60-80b3-3d2533f84357",
#                         "searchMatches":  [

#                                           ],
#                         "indexingPreset":  "Default",
#                         "streamingPreset":  "SingleBitrate",
#                         "sourceLanguage":  "en-US",
#                         "sourceLanguages":  [
#                                                 "en-US"
#                                             ],
#                         "personModelId":  "00000000-0000-0000-0000-000000000000"
#                     }
#                 ],
#     "nextPage":  {
#                      "pageSize":  25,
#                      "skip":  0,
#                      "done":  true,
#                      "totalCount":  1
#                  }
# }