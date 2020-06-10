---
layout: post
title:  "How to start a standalone node with load generation"
date:   2020-06-10
author: Hidenori
---

# Start a standalone node

Create `stellar-core/stellar-core.cfg` and copy and paste the following:

```
HTTP_PORT=8080
PUBLIC_HTTP_PORT=false
RUN_STANDALONE=true

NETWORK_PASSPHRASE="My local test network"

NODE_SEED="SDQVDISRYN2JXBS7ICL7QJAEKB3HWBJFP2QECXG7GZICAHBK4UNJCWK2 self"
NODE_IS_VALIDATOR=true

ARTIFICIALLY_GENERATE_LOAD_FOR_TESTING=true

DATABASE="sqlite3://stellar.db"

COMMANDS=["ll?level=info"]

FAILURE_SAFETY=0
UNSAFE_QUORUM=true

[QUORUM_SET]
THRESHOLD_PERCENT=100
VALIDATORS=["$self"]

[HISTORY.vs]
get="cp /tmp/stellar-core/history/vs/{0} {1}"
put="cp {0} /tmp/stellar-core/history/vs/{1}"
mkdir="mkdir -p /tmp/stellar-core/history/vs/{0}"
```

Run `make install -j3; stellar-core new-db; stellar-core force-scp; stellar-core run` from `stellar-core/`.

# Load generation

Run the following:

```
stellar-core http-command "upgrades?mode=set&upgradetime=$(date +%FT%TZ)&maxtxsize=1000000";
sleep 2;
stellar-core http-command generateload;
sleep 10;
stellar-core http-command "generateload?mode=pay&txs=500000&txrate=29&spikeinterval=7&spikesize=789"
```

after modifying `txs`, `txrate`, `spikeinterval` and `spikesize` to what you want.

# Metrics

Access [http://127.0.0.1:8080/metrics](http://127.0.0.1:8080/metrics) to see metrics.
`ledger.transaction.apply` might be worth checking.

