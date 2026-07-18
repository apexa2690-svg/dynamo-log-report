# Access log report

Read /app/access.log and create /app/report.json.

Each non-empty line is one request. The first value is the client IP. The
requested path is the part between the HTTP method and HTTP version.

Use this JSON format:

{
  "total_requests": 0,
  "unique_ips": 0,
  "top_path": "/example"
}

## Success criteria

1. Create /app/report.json as a valid JSON object.
2. Include only total_requests, unique_ips, and top_path. The first two values
   must be integers, and top_path must be a string.
3. Count all non-empty log lines in total_requests.
4. Count all different client IPs in unique_ips.
5. Put the most requested path in top_path.
