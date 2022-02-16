EPOCH_TIMESTAMP=$(($(date +%s)*1000))
aws logs put-log-events \
      --log-group-name "ProgramaticLog" \
      --log-stream-name "$EPOCH_TIMESTAMP" \
      --log-events \
      message=hello

aws logs put-log-events \
    --log-group-name "ProgramaticLog" \ 
    --log-stream-name "TestStream" \ 
    message=hello