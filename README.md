adk web --port 9000

adk api_server --port 9000


LIST APPS:
curl -X GET http://localhost:8000/list-apps

SET Session 
curl -X POST "http://127.0.0.1:8000/apps/agent1/users/u_123/sessions/s_123" -H "Content-Type: application/json" -d "{}"      

--RUN
curl -X POST "http://localhost:8000/run" -H "Content-Type: application/json" -d "{\"app_name\": \"agent1\", \"user_id\": \"u_123\", \"session_id\": \"s_123\", \"new_message\": {\"role\": \"user\", \"parts\": [{\"text\": \"Hey whats the weather in new york today\"}]}}"
"# googleadk" 
