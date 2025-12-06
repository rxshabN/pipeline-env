from hud_controller.spec import EnvironmentState, Grade, problem
from hud_controller.graders import AgentPatchGrader

# AUTOMATICALLY GENERATED FROM hud_tasks.json

@problem(
    id="transmission-05aef3e",
    description="""
    refactor: unify quarks and strings to snake_case (#7108)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="030b22f91cc3bb76b8b8f26b30aacd3b828b6cf6",
    test="05aef3e78799456cf608d940f5e8f5deddd22772", 
    golden="05aef3e78799456cf608d940f5e8f5deddd22772",
)
def transmission_05aef3e(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="030b22f91cc3bb76b8b8f26b30aacd3b828b6cf6",
            test="05aef3e78799456cf608d940f5e8f5deddd22772", 
            golden="05aef3e78799456cf608d940f5e8f5deddd22772",
            jest_test_files=["cli/cli.cc", "docs/Blocklists.md", "docs/Editing-Configuration-Files.md", "docs/Headless-Usage.md", "docs/Transmission-Resume-Files.md", "docs/rpc-spec.md", "gtk/Actions.cc", "gtk/DetailsDialog.cc", "gtk/PrefsDialog.cc", "gtk/Session.cc", "gtk/transmission-ui.xml", "libtransmission/quark.cc", "libtransmission/quark.h", "libtransmission/resume.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/stats.cc", "libtransmission/transmission.h", "libtransmission/variant.cc", "libtransmission/variant.h", "news/news-5.0.0-draft.md", "qt/DetailsDialog.cc", "qt/FreeSpaceLabel.cc", "qt/OptionsDialog.cc", "qt/Prefs.cc", "qt/PrefsDialog.cc", "qt/Session.cc", "qt/Torrent.cc", "qt/VariantHelpers.cc", "tests/libtransmission/completion-test.cc", "tests/libtransmission/json-test.cc", "tests/libtransmission/rpc-test.cc", "utils/remote.cc", "web/src/file-row.js", "web/src/inspector.js", "web/src/open-dialog.js", "web/src/prefs-dialog.js", "web/src/remote.js", "web/src/statistics-dialog.js", "web/src/torrent.js", "web/src/transmission.js"], 
        )
    ])

@problem(
    id="transmission-1cb24a7",
    description="""
    feat: new JSON-RPC 2.0 RPC API (#7269)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d64a1a5699b4a3dd70aaf4cf28070ee9e3759d29",
    test="1cb24a701b437a992203da91a2694fdea97ca5f3", 
    golden="1cb24a701b437a992203da91a2694fdea97ca5f3",
)
def transmission_1cb24a7(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d64a1a5699b4a3dd70aaf4cf28070ee9e3759d29",
            test="1cb24a701b437a992203da91a2694fdea97ca5f3", 
            golden="1cb24a701b437a992203da91a2694fdea97ca5f3",
            jest_test_files=["docs/rpc-spec.md", "libtransmission/quark.cc", "libtransmission/quark.h", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/rpcimpl.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/transmission.h", "tests/libtransmission/rpc-test.cc", "web/src/open-dialog.js", "web/src/prefs-dialog.js", "web/src/remote.js", "web/src/rename-dialog.js", "web/src/statistics-dialog.js", "web/src/transmission.js"], 
        )
    ])

@problem(
    id="transmission-25d2ebf",
    description="""
    refactor: overhaul `tr_address` special address checks (#7818)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="40e1bd660dddaba03bf071e5ce4d141e800e7ec4",
    test="25d2ebf8fc7677b2b4f65390a9169cc94a2eeb37", 
    golden="25d2ebf8fc7677b2b4f65390a9169cc94a2eeb37",
)
def transmission_25d2ebf(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="40e1bd660dddaba03bf071e5ce4d141e800e7ec4",
            test="25d2ebf8fc7677b2b4f65390a9169cc94a2eeb37", 
            golden="25d2ebf8fc7677b2b4f65390a9169cc94a2eeb37",
            jest_test_files=["libtransmission/announcer-udp.cc", "libtransmission/ip-cache.cc", "libtransmission/net.cc", "libtransmission/net.h", "libtransmission/peer-msgs.cc", "libtransmission/session.cc", "libtransmission/tr-udp.cc", "tests/libtransmission/ip-cache-test.cc", "tests/libtransmission/net-test.cc"], 
        )
    ])

@problem(
    id="transmission-4318a6f",
    description="""
    fix: caching a source address doesn't imply public internet connectivity (#7520)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="8d25484cdbc131f2a47db704b82ef9a8ec98cea7",
    test="4318a6f1ac1eda1cbaae9472d76b6119503dbf8a", 
    golden="4318a6f1ac1eda1cbaae9472d76b6119503dbf8a",
)
def transmission_4318a6f(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="8d25484cdbc131f2a47db704b82ef9a8ec98cea7",
            test="4318a6f1ac1eda1cbaae9472d76b6119503dbf8a", 
            golden="4318a6f1ac1eda1cbaae9472d76b6119503dbf8a",
            jest_test_files=["libtransmission/ip-cache.cc", "libtransmission/ip-cache.h", "libtransmission/net.h", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/tr-udp.cc", "tests/libtransmission/ip-cache-test.cc"], 
        )
    ])

@problem(
    id="transmission-0f7f460",
    description="""
    feat: allow downloading sequentially from a specific piece (#7502)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="af92dc5d80155fe15ced85d6c9306cb122a15e18",
    test="0f7f460c5589c5511c18140c321df5f85c0b7233", 
    golden="0f7f460c5589c5511c18140c321df5f85c0b7233",
)
def transmission_0f7f460(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="af92dc5d80155fe15ced85d6c9306cb122a15e18",
            test="0f7f460c5589c5511c18140c321df5f85c0b7233", 
            golden="0f7f460c5589c5511c18140c321df5f85c0b7233",
            jest_test_files=["docs/rpc-spec.md", "libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-mgr-wishlist.h", "libtransmission/peer-mgr.cc", "libtransmission/quark.cc", "libtransmission/quark.h", "libtransmission/resume.cc", "libtransmission/resume.h", "libtransmission/rpcimpl.cc", "libtransmission/torrent-ctor.h", "libtransmission/torrent.h", "tests/libtransmission/peer-mgr-wishlist-test.cc"], 
        )
    ])

@problem(
    id="transmission-2a3a8ea",
    description="""
    perf: even faster wishlist (#7744)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="50e0ffb910df5caff8b0851da7bf46edff133e8b",
    test="2a3a8ea3643d1ecb654f6ff38fa03b7e6683a8b1", 
    golden="2a3a8ea3643d1ecb654f6ff38fa03b7e6683a8b1",
)
def transmission_2a3a8ea(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="50e0ffb910df5caff8b0851da7bf46edff133e8b",
            test="2a3a8ea3643d1ecb654f6ff38fa03b7e6683a8b1", 
            golden="2a3a8ea3643d1ecb654f6ff38fa03b7e6683a8b1",
            jest_test_files=["libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-mgr-wishlist.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "tests/libtransmission/peer-mgr-wishlist-test.cc"], 
        )
    ])

@problem(
    id="transmission-41dd2cf",
    description="""
    fix: accept either one of udp announce response (#7583)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f26eca5fd5706ffb7d93a4a6dc48a48fb0d321ad",
    test="41dd2cfd530e9eba666485709f20b91be46f64ee", 
    golden="41dd2cfd530e9eba666485709f20b91be46f64ee",
)
def transmission_41dd2cf(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f26eca5fd5706ffb7d93a4a6dc48a48fb0d321ad",
            test="41dd2cfd530e9eba666485709f20b91be46f64ee", 
            golden="41dd2cfd530e9eba666485709f20b91be46f64ee",
            jest_test_files=["libtransmission/announcer-common.h", "libtransmission/announcer-udp.cc", "tests/libtransmission/announcer-udp-test.cc"], 
        )
    ])

@problem(
    id="transmission-454b810",
    description="""
    fix: performance-for-range-copy warning in tr-peer-info-test.cc (#7741)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d31e77a494eaac4c03376680ad453365f2c8db0a",
    test="454b810698a94ee6d5b643fc143f9b2c22521cb7", 
    golden="454b810698a94ee6d5b643fc143f9b2c22521cb7",
)
def transmission_454b810(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d31e77a494eaac4c03376680ad453365f2c8db0a",
            test="454b810698a94ee6d5b643fc143f9b2c22521cb7", 
            golden="454b810698a94ee6d5b643fc143f9b2c22521cb7",
            jest_test_files=["tests/libtransmission/tr-peer-info-test.cc"], 
        )
    ])

@problem(
    id="transmission-0715897",
    description="""
    feat: use canonical peer priority to decide which peers to keep (#6981)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="e7d4a69107059eef19225300af309e81abdd992b",
    test="0715897fc8a998db0f9a6cbb25f9119b1d9b41f3", 
    golden="0715897fc8a998db0f9a6cbb25f9119b1d9b41f3",
)
def transmission_0715897(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="e7d4a69107059eef19225300af309e81abdd992b",
            test="0715897fc8a998db0f9a6cbb25f9119b1d9b41f3", 
            golden="0715897fc8a998db0f9a6cbb25f9119b1d9b41f3",
            jest_test_files=[".github/workflows/actions.yml", ".gitmodules", "CMakeLists.txt", "Transmission.xcodeproj/project.pbxproj", "cmake/FindCRC32C.cmake", "libtransmission/CMakeLists.txt", "libtransmission/crypto-utils.cc", "libtransmission/crypto-utils.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-mgr.h", "libtransmission/peer-msgs.cc", "tests/libtransmission/tr-peer-info-test.cc", "third-party/crc32c", "third-party/macosx-crc32c-config.h"], 
        )
    ])

@problem(
    id="transmission-e7d4a69",
    description="""
    fix: update wishlist when files wanted changed (#7733)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c4dc244212f7b55a1865ff2e263f81458f490544",
    test="e7d4a69107059eef19225300af309e81abdd992b", 
    golden="e7d4a69107059eef19225300af309e81abdd992b",
)
def transmission_e7d4a69(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c4dc244212f7b55a1865ff2e263f81458f490544",
            test="e7d4a69107059eef19225300af309e81abdd992b", 
            golden="e7d4a69107059eef19225300af309e81abdd992b",
            jest_test_files=["libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-mgr-wishlist.h", "libtransmission/peer-mgr.cc", "libtransmission/torrent.h", "tests/libtransmission/peer-mgr-wishlist-test.cc"], 
        )
    ])

@problem(
    id="transmission-894c085",
    description="""
    ci: run clang-tidy for tests (#7526)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="58c4386dddb8c63cd0a63ab3a476a2446b85b1fe",
    test="894c0859aa3e4e5ee2425d856b7a5315add3bd12", 
    golden="894c0859aa3e4e5ee2425d856b7a5315add3bd12",
)
def transmission_894c085(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="58c4386dddb8c63cd0a63ab3a476a2446b85b1fe",
            test="894c0859aa3e4e5ee2425d856b7a5315add3bd12", 
            golden="894c0859aa3e4e5ee2425d856b7a5315add3bd12",
            jest_test_files=[".github/workflows/actions.yml", "tests/libtransmission/file-test.cc"], 
        )
    ])

@problem(
    id="transmission-bf5507f",
    description="""
    fix: load `.torrent` then `.magnet` (#7585)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d0c26cc6123bad38d5e175c2503017fead6e03f5",
    test="bf5507ff2411ede230af098eac1fb0dd0d994262", 
    golden="bf5507ff2411ede230af098eac1fb0dd0d994262",
)
def transmission_bf5507f(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d0c26cc6123bad38d5e175c2503017fead6e03f5",
            test="bf5507ff2411ede230af098eac1fb0dd0d994262", 
            golden="bf5507ff2411ede230af098eac1fb0dd0d994262",
            jest_test_files=["libtransmission/session.cc", "tests/libtransmission/assets/archlinux-2025.05.01-x86_64.iso.magnet", "tests/libtransmission/assets/archlinux-2025.05.01-x86_64.iso.torrent", "tests/libtransmission/session-test.cc"], 
        )
    ])

@problem(
    id="transmission-08ec7fb",
    description="""
    build: lint header files with clang-tidy (#7527)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f0c8fd689aed98275c3c2ef5bd200271c8dd7204",
    test="08ec7fb7c7b9c77ba52ff84d853833d70fd6f59b", 
    golden="08ec7fb7c7b9c77ba52ff84d853833d70fd6f59b",
)
def transmission_08ec7fb(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f0c8fd689aed98275c3c2ef5bd200271c8dd7204",
            test="08ec7fb7c7b9c77ba52ff84d853833d70fd6f59b", 
            golden="08ec7fb7c7b9c77ba52ff84d853833d70fd6f59b",
            jest_test_files=[".gitattributes", "gtk/main.cc", "libtransmission/.clang-tidy", "libtransmission/announce-list.h", "libtransmission/announcer.h", "libtransmission/benc.h", "libtransmission/block-info.h", "libtransmission/completion.h", "libtransmission/crypto-utils.h", "libtransmission/error.h", "libtransmission/handshake.h", "libtransmission/interned-string.h", "libtransmission/log.cc", "libtransmission/log.h", "libtransmission/makemeta.h", "libtransmission/mime-types.h", "libtransmission/mime-types.js", "libtransmission/net.cc", "libtransmission/net.h", "libtransmission/observable.h", "libtransmission/peer-common.h", "libtransmission/peer-io.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-mgr.h", "libtransmission/peer-mse.h", "libtransmission/peer-msgs.cc", "libtransmission/peer-msgs.h", "libtransmission/peer-socket.h", "libtransmission/platform.h", "libtransmission/port-forwarding-natpmp.h", "libtransmission/port-forwarding-upnp.cc", "libtransmission/port-forwarding-upnp.h", "libtransmission/port-forwarding.h", "libtransmission/quark.h", "libtransmission/rpc-server.h", "libtransmission/session-alt-speeds.h", "libtransmission/session-id.h", "libtransmission/session-thread.h", "libtransmission/session.h", "libtransmission/stats.h", "libtransmission/torrent-queue.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/tr-arc4.h", "libtransmission/tr-buffer.h", "libtransmission/tr-getopt.h", "libtransmission/tr-macros.h", "libtransmission/tr-popcount.h", "libtransmission/tr-strbuf.h", "libtransmission/transmission.h", "libtransmission/utils.cc", "libtransmission/values.h", "libtransmission/variant.h", "libtransmission/verify.h", "libtransmission/version.h.in", "libtransmission/watchdir-base.h", "libtransmission/watchdir.h", "libtransmission/web-utils.cc", "libtransmission/web-utils.h", "libtransmission/web.h", "libtransmission/webseed.h", "macosx/Controller.mm", "macosx/MessageWindowController.mm", "qt/.clang-tidy", "qt/Application.cc", "qt/Prefs.cc", "tests/libtransmission/.clang-tidy", "tests/libtransmission/announce-list-test.cc", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/move-test.cc", "tests/libtransmission/remove-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/torrent-metainfo-test.cc", "tests/libtransmission/utils-test.cc", "tests/libtransmission/variant-test.cc", "tests/libtransmission/watchdir-test.cc", "utils/remote.cc"], 
        )
    ])

@problem(
    id="transmission-9e15394",
    description="""
    refactor: announcer code housekeeping (#7496)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="03c2dbd63ccdf3e9051f98b6d0d6ded2adc803f8",
    test="9e15394c65ecddf1b15f7225fa7a4fa29e302505", 
    golden="9e15394c65ecddf1b15f7225fa7a4fa29e302505",
)
def transmission_9e15394(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="03c2dbd63ccdf3e9051f98b6d0d6ded2adc803f8",
            test="9e15394c65ecddf1b15f7225fa7a4fa29e302505", 
            golden="9e15394c65ecddf1b15f7225fa7a4fa29e302505",
            jest_test_files=["libtransmission/announcer-common.h", "libtransmission/announcer-http.cc", "libtransmission/announcer-udp.cc", "libtransmission/announcer.cc", "tests/libtransmission/announcer-test.cc", "tests/libtransmission/announcer-udp-test.cc"], 
        )
    ])

@problem(
    id="transmission-03c2dbd",
    description="""
    feat: make `proxy_url` nullable (#7486)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="cf7ac07a6cef093127e3aaae00a79413e190ce7c",
    test="03c2dbd63ccdf3e9051f98b6d0d6ded2adc803f8", 
    golden="03c2dbd63ccdf3e9051f98b6d0d6ded2adc803f8",
)
def transmission_03c2dbd(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="cf7ac07a6cef093127e3aaae00a79413e190ce7c",
            test="03c2dbd63ccdf3e9051f98b6d0d6ded2adc803f8", 
            golden="03c2dbd63ccdf3e9051f98b6d0d6ded2adc803f8",
            jest_test_files=["docs/Editing-Configuration-Files.md", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/settings.cc", "libtransmission/web.cc", "libtransmission/web.h", "tests/libtransmission/settings-test.cc"], 
        )
    ])

@problem(
    id="transmission-76d854d",
    description="""
    fix: clang-tidy-20 warnings (#7479)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="7e87adcd918c7de8fbb0b6df9bb5399e45b5196c",
    test="76d854dcc89f1fec252e678dc09ec73c4d776f24", 
    golden="76d854dcc89f1fec252e678dc09ec73c4d776f24",
)
def transmission_76d854d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="7e87adcd918c7de8fbb0b6df9bb5399e45b5196c",
            test="76d854dcc89f1fec252e678dc09ec73c4d776f24", 
            golden="76d854dcc89f1fec252e678dc09ec73c4d776f24",
            jest_test_files=["libtransmission/file-posix.cc", "qt/.clang-tidy", "qt/Application.cc", "tests/libtransmission/.clang-tidy", "tests/libtransmission/block-info-test.cc", "tests/libtransmission/completion-test.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/file-piece-map-test.cc", "tests/libtransmission/ip-cache-test.cc", "tests/libtransmission/session-test.cc", "tests/libtransmission/subprocess-test.cc", "tests/libtransmission/timer-test.cc"], 
        )
    ])

@problem(
    id="transmission-24f58f7",
    description="""
    feat: sequential download in `settings.json` `torrent-add` and `sesssion-*` RPC methods (#7047)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="04769d998619d59a99b9e25e0cf2c398e61547ef",
    test="24f58f70ee2bf96bfb93fe9c3f9e8d6c90cb2bd9", 
    golden="24f58f70ee2bf96bfb93fe9c3f9e8d6c90cb2bd9",
)
def transmission_24f58f7(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="04769d998619d59a99b9e25e0cf2c398e61547ef",
            test="24f58f70ee2bf96bfb93fe9c3f9e8d6c90cb2bd9", 
            golden="24f58f70ee2bf96bfb93fe9c3f9e8d6c90cb2bd9",
            jest_test_files=["docs/Editing-Configuration-Files.md", "docs/rpc-spec.md", "libtransmission/resume.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.h", "libtransmission/torrent-ctor.h", "libtransmission/torrent.cc", "tests/libtransmission/rpc-test.cc"], 
        )
    ])

@problem(
    id="transmission-088232f",
    description="""
    fix: abort handshake if the torrent is stopped (#6947)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1232f558a635766f697bf08c81f90cefae2504e0",
    test="088232f69cbfbc6cef9fd18291f04d5c2aa5d5f4", 
    golden="088232f69cbfbc6cef9fd18291f04d5c2aa5d5f4",
)
def transmission_088232f(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1232f558a635766f697bf08c81f90cefae2504e0",
            test="088232f69cbfbc6cef9fd18291f04d5c2aa5d5f4", 
            golden="088232f69cbfbc6cef9fd18291f04d5c2aa5d5f4",
            jest_test_files=["libtransmission/handshake.cc", "libtransmission/handshake.h", "libtransmission/peer-mgr.cc", "tests/libtransmission/handshake-test.cc"], 
        )
    ])

@problem(
    id="transmission-47eb4ee",
    description="""
    refactor: dedicated class for torrent queue (#7332)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="4e7fc8197586c1edc44f9a9f3177c755fcbfdd6b",
    test="47eb4ee2bcadaf760b6aabe175f56e137a5531b1", 
    golden="47eb4ee2bcadaf760b6aabe175f56e137a5531b1",
)
def transmission_47eb4ee(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="4e7fc8197586c1edc44f9a9f3177c755fcbfdd6b",
            test="47eb4ee2bcadaf760b6aabe175f56e137a5531b1", 
            golden="47eb4ee2bcadaf760b6aabe175f56e137a5531b1",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "libtransmission/CMakeLists.txt", "libtransmission/quark.cc", "libtransmission/quark.h", "libtransmission/resume.cc", "libtransmission/resume.h", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent-metainfo.h", "libtransmission/torrent-queue.cc", "libtransmission/torrent-queue.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/torrent-queue-test.cc"], 
        )
    ])

@problem(
    id="transmission-cbd65ae",
    description="""
    refactor: fix modernize-use-nodiscard warnings by adding [[nodiscard]] (#7351)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="de782e43153489f21f7b2686cec4519ae2af4412",
    test="cbd65ae8b1f16ac639e725aa40751fb894cebaa9", 
    golden="cbd65ae8b1f16ac639e725aa40751fb894cebaa9",
)
def transmission_cbd65ae(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="de782e43153489f21f7b2686cec4519ae2af4412",
            test="cbd65ae8b1f16ac639e725aa40751fb894cebaa9", 
            golden="cbd65ae8b1f16ac639e725aa40751fb894cebaa9",
            jest_test_files=["libtransmission/benc.h", "qt/AddData.h", "qt/DBusInteropHelper.h", "qt/FileTreeDelegate.h", "qt/FileTreeModel.h", "qt/FileTreeView.h", "qt/FilterBarComboBox.h", "qt/FilterBarComboBoxDelegate.h", "qt/Filters.h", "qt/IconToolButton.h", "qt/InteropHelper.h", "qt/InteropObject.h", "qt/MainWindow.h", "qt/MakeDialog.h", "qt/PathButton.h", "qt/Torrent.h", "qt/TorrentFilter.h", "qt/TrackerDelegate.h", "qt/TrackerModel.h", "qt/TrackerModelFilter.h", "qt/WatchDir.h", "tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-50eacf6",
    description="""
    Consume early pad a/b, improve handshake tests (#6987)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="cbba2e0390e6972fdc14eb95ef0e28f485aa4112",
    test="50eacf693365e96306db15a932ea5f8d70ad69ba", 
    golden="50eacf693365e96306db15a932ea5f8d70ad69ba",
)
def transmission_50eacf6(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="cbba2e0390e6972fdc14eb95ef0e28f485aa4112",
            test="50eacf693365e96306db15a932ea5f8d70ad69ba", 
            golden="50eacf693365e96306db15a932ea5f8d70ad69ba",
            jest_test_files=["libtransmission/handshake.cc", "libtransmission/handshake.h", "tests/libtransmission/handshake-test.cc"], 
        )
    ])

@problem(
    id="transmission-b3912fa",
    description="""
    feat: download first and last piece first in sequential mode (#6893)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b4bbc8744e06ab921a5a837fcd35b87795c0eb7d",
    test="b3912fa1a5a4c68f412eb65ebf5fde437df71d03", 
    golden="b3912fa1a5a4c68f412eb65ebf5fde437df71d03",
)
def transmission_b3912fa(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b4bbc8744e06ab921a5a837fcd35b87795c0eb7d",
            test="b3912fa1a5a4c68f412eb65ebf5fde437df71d03", 
            golden="b3912fa1a5a4c68f412eb65ebf5fde437df71d03",
            jest_test_files=["libtransmission/peer-mgr-wishlist.cc", "tests/libtransmission/peer-mgr-wishlist-test.cc"], 
        )
    ])

@problem(
    id="transmission-90859fe",
    description="""
    test: use new `tr_variant` API (#7268)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="510286f419c991706569f5aa5894a4ca89b1537f",
    test="90859fe115c2f6d8e019bd918972e4966f34c1e5", 
    golden="90859fe115c2f6d8e019bd918972e4966f34c1e5",
)
def transmission_90859fe(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="510286f419c991706569f5aa5894a4ca89b1537f",
            test="90859fe115c2f6d8e019bd918972e4966f34c1e5", 
            golden="90859fe115c2f6d8e019bd918972e4966f34c1e5",
            jest_test_files=["libtransmission/variant.h", "tests/libtransmission/dht-test.cc", "tests/libtransmission/json-test.cc", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/move-test.cc", "tests/libtransmission/rpc-test.cc", "tests/libtransmission/session-test.cc", "tests/libtransmission/settings-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/variant-test.cc"], 
        )
    ])

@problem(
    id="transmission-60e5d98",
    description="""
    fix: handle nullptr in json serde (#7258)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="affb03a8d2c7393b54542439c9c5dcfb4ded01ae",
    test="60e5d98dc1fc4c40e817eb6c0fa6baa34c6be93e", 
    golden="60e5d98dc1fc4c40e817eb6c0fa6baa34c6be93e",
)
def transmission_60e5d98(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="affb03a8d2c7393b54542439c9c5dcfb4ded01ae",
            test="60e5d98dc1fc4c40e817eb6c0fa6baa34c6be93e", 
            golden="60e5d98dc1fc4c40e817eb6c0fa6baa34c6be93e",
            jest_test_files=["libtransmission/variant-json.cc", "tests/libtransmission/json-test.cc"], 
        )
    ])

@problem(
    id="transmission-affb03a",
    description="""
    refactor: remove `tr_torrent::do_magnet_idle_work()` (#7271)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="43f5ca8e0c15c5c9e80326835bf02524b5eace48",
    test="affb03a8d2c7393b54542439c9c5dcfb4ded01ae", 
    golden="affb03a8d2c7393b54542439c9c5dcfb4ded01ae",
)
def transmission_affb03a(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="43f5ca8e0c15c5c9e80326835bf02524b5eace48",
            test="affb03a8d2c7393b54542439c9c5dcfb4ded01ae", 
            golden="affb03a8d2c7393b54542439c9c5dcfb4ded01ae",
            jest_test_files=["libtransmission/torrent-magnet.cc", "libtransmission/torrent-magnet.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "tests/libtransmission/torrent-magnet-test.cc"], 
        )
    ])

@problem(
    id="transmission-7e4b4f1",
    description="""
    refactor: faster wishlist (#7027)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="198ee5bd97acd62fcbc62bb8e765b761667c0532",
    test="7e4b4f10a1f90885c0bebb168eedffe153f1cf53", 
    golden="7e4b4f10a1f90885c0bebb168eedffe153f1cf53",
)
def transmission_7e4b4f1(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="198ee5bd97acd62fcbc62bb8e765b761667c0532",
            test="7e4b4f10a1f90885c0bebb168eedffe153f1cf53", 
            golden="7e4b4f10a1f90885c0bebb168eedffe153f1cf53",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "libtransmission/CMakeLists.txt", "libtransmission/peer-common.h", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "libtransmission/peer-mgr-active-requests.cc", "libtransmission/peer-mgr-active-requests.h", "libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-mgr-wishlist.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-mgr.h", "libtransmission/peer-msgs.cc", "libtransmission/torrent.h", "libtransmission/webseed.cc", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/peer-mgr-active-requests-test.cc", "tests/libtransmission/peer-mgr-wishlist-test.cc"], 
        )
    ])

@problem(
    id="transmission-6224039",
    description="""
    feat: configurable client `reqq` (#7030)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b0a6bf964c0fa8e5fe0006e3c9dafc7ba236d22d",
    test="62240393ed056099a6a2ee60d778ac19928ef451", 
    golden="62240393ed056099a6a2ee60d778ac19928ef451",
)
def transmission_6224039(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b0a6bf964c0fa8e5fe0006e3c9dafc7ba236d22d",
            test="62240393ed056099a6a2ee60d778ac19928ef451", 
            golden="62240393ed056099a6a2ee60d778ac19928ef451",
            jest_test_files=["docs/Editing-Configuration-Files.md", "docs/rpc-spec.md", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.h", "tests/libtransmission/rpc-test.cc"], 
        )
    ])

@problem(
    id="transmission-b0a6bf9",
    description="""
    perf: lazy initialise Diffie-Hellman in handshake (#6949)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b5b7d7abdec6ca2e59ea8deb0d4435342805f83a",
    test="b0a6bf964c0fa8e5fe0006e3c9dafc7ba236d22d", 
    golden="b0a6bf964c0fa8e5fe0006e3c9dafc7ba236d22d",
)
def transmission_b0a6bf9(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b5b7d7abdec6ca2e59ea8deb0d4435342805f83a",
            test="b0a6bf964c0fa8e5fe0006e3c9dafc7ba236d22d", 
            golden="b0a6bf964c0fa8e5fe0006e3c9dafc7ba236d22d",
            jest_test_files=["libtransmission/handshake.cc", "libtransmission/handshake.h", "libtransmission/peer-mse.cc", "libtransmission/peer-mse.h", "tests/libtransmission/crypto-test.cc"], 
        )
    ])

@problem(
    id="transmission-3e5a77d",
    description="""
    refactor: remove last byte special case in `tr_block_info::byte_loc()` (#7064)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="10333d23b21422e1e8e8e92bc74ad5b491b2dccd",
    test="3e5a77d17603dd6548add3c5b233a4e87d38c577", 
    golden="3e5a77d17603dd6548add3c5b233a4e87d38c577",
)
def transmission_3e5a77d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="10333d23b21422e1e8e8e92bc74ad5b491b2dccd",
            test="3e5a77d17603dd6548add3c5b233a4e87d38c577", 
            golden="3e5a77d17603dd6548add3c5b233a4e87d38c577",
            jest_test_files=["libtransmission/block-info.h", "libtransmission/file-piece-map.cc", "libtransmission/torrent.cc", "tests/libtransmission/file-piece-map-test.cc"], 
        )
    ])

@problem(
    id="transmission-9fc9daf",
    description="""
    Fails with an error if data removal was not possible (#6055)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="abfd39065c39e955dedd1a74ebbe03fe5d0ea45d",
    test="9fc9daf40dc671d6215a9b254abadcbfdf4f00b4", 
    golden="9fc9daf40dc671d6215a9b254abadcbfdf4f00b4",
)
def transmission_9fc9daf(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="abfd39065c39e955dedd1a74ebbe03fe5d0ea45d",
            test="9fc9daf40dc671d6215a9b254abadcbfdf4f00b4", 
            golden="9fc9daf40dc671d6215a9b254abadcbfdf4f00b4",
            jest_test_files=["gtk/OptionsDialog.cc", "gtk/Session.cc", "libtransmission/rpcimpl.cc", "libtransmission/torrent-files.cc", "libtransmission/torrent-files.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/transmission.h", "libtransmission/utils.cc", "libtransmission/utils.h", "macosx/Torrent.mm", "tests/libtransmission/move-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/rpc-test.cc"], 
        )
    ])

@problem(
    id="transmission-fa8be1b",
    description="""
    fix: `tr_variant_serde::parse_json()` bug fixes (#6901)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c21ee87eea24eadaf4acd3eb58c837bad223018d",
    test="fa8be1b9817f1f649c6becc5c6bea8190df4c0ff", 
    golden="fa8be1b9817f1f649c6becc5c6bea8190df4c0ff",
)
def transmission_fa8be1b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c21ee87eea24eadaf4acd3eb58c837bad223018d",
            test="fa8be1b9817f1f649c6becc5c6bea8190df4c0ff", 
            golden="fa8be1b9817f1f649c6becc5c6bea8190df4c0ff",
            jest_test_files=["libtransmission/variant-json.cc", "tests/libtransmission/variant-test.cc"], 
        )
    ])

@problem(
    id="transmission-a76a07a",
    description="""
    chore: misc code cleanups (#6927)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="7f79cb16ee194d58ce665f9319524bc5e6e4f91d",
    test="a76a07ae992eb7a31435b7087c8ecfba50c1c33c", 
    golden="a76a07ae992eb7a31435b7087c8ecfba50c1c33c",
)
def transmission_a76a07a(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="7f79cb16ee194d58ce665f9319524bc5e6e4f91d",
            test="a76a07ae992eb7a31435b7087c8ecfba50c1c33c", 
            golden="a76a07ae992eb7a31435b7087c8ecfba50c1c33c",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "libtransmission/CMakeLists.txt", "libtransmission/announcer-udp.cc", "libtransmission/global-ip-cache.cc", "libtransmission/global-ip-cache.h", "libtransmission/ip-cache.cc", "libtransmission/ip-cache.h", "libtransmission/session.cc", "libtransmission/session.h", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/global-ip-cache-test.cc", "tests/libtransmission/ip-cache-test.cc"], 
        )
    ])

@problem(
    id="transmission-2c2011d",
    description="""
    fix: update partial file suffix after verifying torrent (#6871)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="acee39e15cae8cff0ab398ade9098baf6dedbf59",
    test="2c2011d40f36e4fbc1ed487b7a5ebd42097bb9a1", 
    golden="2c2011d40f36e4fbc1ed487b7a5ebd42097bb9a1",
)
def transmission_2c2011d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="acee39e15cae8cff0ab398ade9098baf6dedbf59",
            test="2c2011d40f36e4fbc1ed487b7a5ebd42097bb9a1", 
            golden="2c2011d40f36e4fbc1ed487b7a5ebd42097bb9a1",
            jest_test_files=["libtransmission/torrent.cc", "libtransmission/torrent.h", "tests/libtransmission/move-test.cc", "tests/libtransmission/rename-test.cc"], 
        )
    ])

@problem(
    id="transmission-4657d21",
    description="""
    feat: dual stack udp tracker support (#6687)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="3677e7a591cbf629bf330542ea0da2ff6ae3aa45",
    test="4657d210bae56aeb492dd28803013398b36f12ba", 
    golden="4657d210bae56aeb492dd28803013398b36f12ba",
)
def transmission_4657d21(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="3677e7a591cbf629bf330542ea0da2ff6ae3aa45",
            test="4657d210bae56aeb492dd28803013398b36f12ba", 
            golden="4657d210bae56aeb492dd28803013398b36f12ba",
            jest_test_files=["libtransmission/announcer-common.h", "libtransmission/announcer-http.cc", "libtransmission/announcer-udp.cc", "libtransmission/announcer.cc", "libtransmission/announcer.h", "libtransmission/net.cc", "libtransmission/net.h", "libtransmission/tr-udp.cc", "libtransmission/web-utils.cc", "libtransmission/web-utils.h", "tests/libtransmission/announcer-udp-test.cc"], 
        )
    ])

@problem(
    id="transmission-d6f5e60",
    description="""
    feat: ipv6 lpd (#6700)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="5f091fac189b8bba498dff23b3aa4ed172c1e324",
    test="d6f5e60a355a1866f2c0ee5635fd8f64b65de1ac", 
    golden="d6f5e60a355a1866f2c0ee5635fd8f64b65de1ac",
)
def transmission_d6f5e60(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="5f091fac189b8bba498dff23b3aa4ed172c1e324",
            test="d6f5e60a355a1866f2c0ee5635fd8f64b65de1ac", 
            golden="d6f5e60a355a1866f2c0ee5635fd8f64b65de1ac",
            jest_test_files=["libtransmission/net.cc", "libtransmission/net.h", "libtransmission/tr-lpd.cc", "tests/libtransmission/lpd-test.cc"], 
        )
    ])

@problem(
    id="transmission-9748f42",
    description="""
    fix: restore portable file path check (#6853)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="adc405e5bebd5026b9e8b7e2c7ceaebdd470e5eb",
    test="9748f42c5a18dcd3119bcdb1ab30b4e9479cd11b", 
    golden="9748f42c5a18dcd3119bcdb1ab30b4e9479cd11b",
)
def transmission_9748f42(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="adc405e5bebd5026b9e8b7e2c7ceaebdd470e5eb",
            test="9748f42c5a18dcd3119bcdb1ab30b4e9479cd11b", 
            golden="9748f42c5a18dcd3119bcdb1ab30b4e9479cd11b",
            jest_test_files=["libtransmission/makemeta.cc", "libtransmission/makemeta.h", "libtransmission/resume.cc", "libtransmission/torrent-files.cc", "libtransmission/torrent-files.h", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent-metainfo.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "macosx/QuickLookPlugin/GeneratePreviewForURL.mm", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/remove-test.cc", "tests/libtransmission/torrent-files-test.cc", "utils/create.cc"], 
        )
    ])

@problem(
    id="transmission-09b67c8",
    description="""
    fix: possible heap-use-after-free with magnet links (#6815)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="740ce3b904b78cf4bec120ebb5a1cfd326375a87",
    test="09b67c84b1f17ed22b7cce0731867e0029c62fbe", 
    golden="09b67c84b1f17ed22b7cce0731867e0029c62fbe",
)
def transmission_09b67c8(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="740ce3b904b78cf4bec120ebb5a1cfd326375a87",
            test="09b67c84b1f17ed22b7cce0731867e0029c62fbe", 
            golden="09b67c84b1f17ed22b7cce0731867e0029c62fbe",
            jest_test_files=["libtransmission/torrent-magnet.cc", "libtransmission/torrent-magnet.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "tests/libtransmission/torrent-magnet-test.cc"], 
        )
    ])

@problem(
    id="transmission-d935d36",
    description="""
    refactor: remove torrent_view virtual class (#6738)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="8944e587f9cf3ac0eebeff68274385674b9a42d5",
    test="d935d364ed12ec5afe9f1253deb209ad35804e85", 
    golden="d935d364ed12ec5afe9f1253deb209ad35804e85",
)
def transmission_d935d36(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="8944e587f9cf3ac0eebeff68274385674b9a42d5",
            test="d935d364ed12ec5afe9f1253deb209ad35804e85", 
            golden="d935d364ed12ec5afe9f1253deb209ad35804e85",
            jest_test_files=["libtransmission/completion.cc", "libtransmission/completion.h", "libtransmission/torrent.h", "tests/libtransmission/completion-test.cc", "tests/libtransmission/lpd-test.cc", "tests/libtransmission/watchdir-test.cc"], 
        )
    ])

@problem(
    id="transmission-2ff3ae0",
    description="""
    fix: more misc `net.cc` fixes (#6735)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="29173741592ed33df315c5b10203a49cf2544f99",
    test="2ff3ae07d1ac0ae9bfa48229b8e5d0bce1446fde", 
    golden="2ff3ae07d1ac0ae9bfa48229b8e5d0bce1446fde",
)
def transmission_2ff3ae0(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="29173741592ed33df315c5b10203a49cf2544f99",
            test="2ff3ae07d1ac0ae9bfa48229b8e5d0bce1446fde", 
            golden="2ff3ae07d1ac0ae9bfa48229b8e5d0bce1446fde",
            jest_test_files=["libtransmission/net.cc", "libtransmission/tr-udp.cc", "libtransmission/web-utils.cc", "tests/libtransmission/announcer-test.cc", "tests/libtransmission/net-test.cc", "tests/libtransmission/web-utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-1568659",
    description="""
    fix: mismatched `class` forward declaration for `struct tr_peer` (#6725)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c223c70644dd056d3b5970eb0dd193b9f6dd7846",
    test="1568659f95b2c881f03bb3c669fa8ba6f9cf52b8", 
    golden="1568659f95b2c881f03bb3c669fa8ba6f9cf52b8",
)
def transmission_1568659(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c223c70644dd056d3b5970eb0dd193b9f6dd7846",
            test="1568659f95b2c881f03bb3c669fa8ba6f9cf52b8", 
            golden="1568659f95b2c881f03bb3c669fa8ba6f9cf52b8",
            jest_test_files=["tests/libtransmission/peer-mgr-active-requests-test.cc"], 
        )
    ])

@problem(
    id="transmission-152f3e9",
    description="""
    refactor: convert `tr_peerMsgsImpl` helper functions to class methods (#6580)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="8709ec60e69a31367da325e17463714aa5a5d2f3",
    test="152f3e91a560213d2355a6dc08865ef068c2b434", 
    golden="152f3e91a560213d2355a6dc08865ef068c2b434",
)
def transmission_152f3e9(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="8709ec60e69a31367da325e17463714aa5a5d2f3",
            test="152f3e91a560213d2355a6dc08865ef068c2b434", 
            golden="152f3e91a560213d2355a6dc08865ef068c2b434",
            jest_test_files=["libtransmission/handshake.cc", "libtransmission/magnet-metainfo.cc", "libtransmission/net.cc", "libtransmission/net.h", "libtransmission/peer-common.h", "libtransmission/peer-mgr-active-requests.cc", "libtransmission/peer-mgr-active-requests.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-mgr.h", "libtransmission/peer-msgs.cc", "libtransmission/peer-msgs.h", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent-metainfo.h", "libtransmission/webseed.cc", "libtransmission/webseed.h", "tests/libtransmission/completion-test.cc"], 
        )
    ])

@problem(
    id="transmission-edc59ba",
    description="""
    fix compatibility with clang-format 18 (#6690)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="8e35e526c6655bd8ab6f1e3b3bc8996a0561c6c7",
    test="edc59ba5d8edfb6016fad3e2da2783ef3ab0bfd3", 
    golden="edc59ba5d8edfb6016fad3e2da2783ef3ab0bfd3",
)
def transmission_edc59ba(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="8e35e526c6655bd8ab6f1e3b3bc8996a0561c6c7",
            test="edc59ba5d8edfb6016fad3e2da2783ef3ab0bfd3", 
            golden="edc59ba5d8edfb6016fad3e2da2783ef3ab0bfd3",
            jest_test_files=["libtransmission/favicon-cache.h", "qt/RpcClient.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/timer-test.cc"], 
        )
    ])

@problem(
    id="transmission-7c11809",
    description="""
    fix: more clang-tidy warnings (#6608)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d362b3f0f209822b50d0db46282fdd8efe9f9e46",
    test="7c118096720f10bba0eefe570a58111eaa91b3b1", 
    golden="7c118096720f10bba0eefe570a58111eaa91b3b1",
)
def transmission_7c11809(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d362b3f0f209822b50d0db46282fdd8efe9f9e46",
            test="7c118096720f10bba0eefe570a58111eaa91b3b1", 
            golden="7c118096720f10bba0eefe570a58111eaa91b3b1",
            jest_test_files=["gtk/.clang-tidy", "gtk/DetailsDialog.cc", "gtk/DynamicPropertyStore.h", "gtk/FilterBar.cc", "gtk/FilterListModel.hh", "gtk/HigWorkarea.h", "gtk/MessageLogWindow.cc", "gtk/PrefsDialog.h", "gtk/Session.cc", "gtk/StatsDialog.cc", "gtk/Torrent.cc", "gtk/Utils.h", "qt/Application.cc", "qt/DetailsDialog.cc", "qt/FileTreeItem.cc", "qt/FileTreeView.cc", "qt/FilterBar.cc", "qt/InteropObject.cc", "qt/MakeDialog.cc", "qt/Prefs.cc", "qt/PrefsDialog.cc", "qt/Session.cc", "qt/Torrent.cc", "qt/TorrentFilter.cc", "qt/TrackerDelegate.cc", "qt/VariantHelpers.cc", "tests/libtransmission/handshake-test.cc", "tests/libtransmission/move-test.cc", "tests/libtransmission/torrent-magnet-test.cc", "tests/libtransmission/variant-test.cc", "tests/libtransmission/watchdir-test.cc"], 
        )
    ])

@problem(
    id="transmission-f06cb37",
    description="""
    feat: added `sleep-per-seconds-during-verify` to settings.json (#6572)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="cf84afda8c68aa5fa6058df7845d426453c5c290",
    test="f06cb37c06900911178961ef4af897549a427fa3", 
    golden="f06cb37c06900911178961ef4af897549a427fa3",
)
def transmission_f06cb37(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="cf84afda8c68aa5fa6058df7845d426453c5c290",
            test="f06cb37c06900911178961ef4af897549a427fa3", 
            golden="f06cb37c06900911178961ef4af897549a427fa3",
            jest_test_files=["docs/Editing-Configuration-Files.md", "libtransmission/quark.cc", "libtransmission/quark.h", "libtransmission/session-settings.h", "libtransmission/session.cc", "libtransmission/variant-converters.cc", "libtransmission/verify.cc", "libtransmission/verify.h", "tests/libtransmission/settings-test.cc"], 
        )
    ])

@problem(
    id="transmission-168d56c",
    description="""
    perf: restore `3.00` wishlist with cached candidates (#6549)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="ca11c33d0510cf6d870e47cd5ef6812135e97ea2",
    test="168d56cefc61871ab40425f23d14ef9163006410", 
    golden="168d56cefc61871ab40425f23d14ef9163006410",
)
def transmission_168d56c(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="ca11c33d0510cf6d870e47cd5ef6812135e97ea2",
            test="168d56cefc61871ab40425f23d14ef9163006410", 
            golden="168d56cefc61871ab40425f23d14ef9163006410",
            jest_test_files=["libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-mgr-wishlist.h", "libtransmission/peer-mgr.cc", "libtransmission/torrent.cc", "libtransmission/torrent.h", "tests/libtransmission/peer-mgr-wishlist-test.cc"], 
        )
    ])

@problem(
    id="transmission-ca11c33",
    description="""
    fix: various DHT bugs (#6569)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1c71ba5c838c9f1c55cf28a279a866df26227ea7",
    test="ca11c33d0510cf6d870e47cd5ef6812135e97ea2", 
    golden="ca11c33d0510cf6d870e47cd5ef6812135e97ea2",
)
def transmission_ca11c33(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1c71ba5c838c9f1c55cf28a279a866df26227ea7",
            test="ca11c33d0510cf6d870e47cd5ef6812135e97ea2", 
            golden="ca11c33d0510cf6d870e47cd5ef6812135e97ea2",
            jest_test_files=["docs/Editing-Configuration-Files.md", "libtransmission/peer-msgs.cc", "libtransmission/session-settings.h", "libtransmission/session.h", "libtransmission/tr-dht.cc", "libtransmission/tr-dht.h", "tests/libtransmission/dht-test.cc"], 
        )
    ])

@problem(
    id="transmission-468de87",
    description="""
    refactor: fix cppcoreguidelines-avoid-do-while warnings (#6527)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="e408aa074122f8f77ddf952d0925c6bf7e141721",
    test="468de87076c3c1fc4cd46026051b2380488b6775", 
    golden="468de87076c3c1fc4cd46026051b2380488b6775",
)
def transmission_468de87(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="e408aa074122f8f77ddf952d0925c6bf7e141721",
            test="468de87076c3c1fc4cd46026051b2380488b6775", 
            golden="468de87076c3c1fc4cd46026051b2380488b6775",
            jest_test_files=["gtk/.clang-tidy", "gtk/FileList.cc", "libtransmission/file-posix.cc", "libtransmission/subprocess-posix.cc", "qt/.clang-tidy", "tests/libtransmission/.clang-tidy", "tests/libtransmission/bitfield-test.cc"], 
        )
    ])

@problem(
    id="transmission-2394789",
    description="""
    fix: performance-enum-size warnings (#6504)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="9d433ff8b4f2f79c5eb4f01804c7efc2d363888b",
    test="239478925f3a6a20dda7f0c3f4a317e8ae15a7f5", 
    golden="239478925f3a6a20dda7f0c3f4a317e8ae15a7f5",
)
def transmission_2394789(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="9d433ff8b4f2f79c5eb4f01804c7efc2d363888b",
            test="239478925f3a6a20dda7f0c3f4a317e8ae15a7f5", 
            golden="239478925f3a6a20dda7f0c3f4a317e8ae15a7f5",
            jest_test_files=["gtk/FileList.cc", "gtk/FilterBar.cc", "gtk/FilterBase.h", "gtk/ListModelAdapter.h", "gtk/Session.h", "gtk/SorterBase.h", "gtk/Torrent.h", "gtk/TorrentFilter.h", "gtk/Utils.h", "libtransmission/announcer-udp.cc", "libtransmission/peer-msgs.cc", "libtransmission/port-forwarding-upnp.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/torrent-metainfo.cc", "libtransmission/tr-dht.cc", "tests/libtransmission/watchdir-test.cc"], 
        )
    ])

@problem(
    id="transmission-9d433ff",
    description="""
    fix: misc-include-cleaner clang-tidy warnings (#6502)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="8d4dcece890f89769dc6ed8819937ad68f6240b3",
    test="9d433ff8b4f2f79c5eb4f01804c7efc2d363888b", 
    golden="9d433ff8b4f2f79c5eb4f01804c7efc2d363888b",
)
def transmission_9d433ff(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="8d4dcece890f89769dc6ed8819937ad68f6240b3",
            test="9d433ff8b4f2f79c5eb4f01804c7efc2d363888b", 
            golden="9d433ff8b4f2f79c5eb4f01804c7efc2d363888b",
            jest_test_files=["gtk/.clang-tidy", "gtk/Actions.cc", "gtk/Application.cc", "gtk/FileList.cc", "gtk/MessageLogWindow.cc", "gtk/PathButton.cc", "gtk/Percents.cc", "gtk/PrefsDialog.cc", "gtk/Session.cc", "gtk/TorrentCellRenderer.cc", "gtk/Utils.cc", "libtransmission/.clang-tidy", "libtransmission/announce-list.cc", "libtransmission/cache.cc", "libtransmission/inout.cc", "libtransmission/tr-utp.cc", "qt/.clang-tidy", "qt/Application.cc", "qt/Formatter.cc", "qt/IconCache.cc", "qt/Prefs.cc", "qt/Session.cc", "qt/TorrentDelegateMin.cc", "qt/Utils.cc", "qt/VariantHelpers.cc", "tests/libtransmission/.clang-tidy", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-df1dc58",
    description="""
    fix: restore the `tag` key in RPC response (#6492)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="4bb9eab0d062073a6fc5ba0995f2e2575250f6a0",
    test="df1dc5812cd5c928570cf957d5efc69753986149", 
    golden="df1dc5812cd5c928570cf957d5efc69753986149",
)
def transmission_df1dc58(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="4bb9eab0d062073a6fc5ba0995f2e2575250f6a0",
            test="df1dc5812cd5c928570cf957d5efc69753986149", 
            golden="df1dc5812cd5c928570cf957d5efc69753986149",
            jest_test_files=["libtransmission/rpcimpl.cc", "tests/libtransmission/rpc-test.cc"], 
        )
    ])

@problem(
    id="transmission-22cde5d",
    description="""
    refactor: use new tr_variant API in rpcimpl (#6456)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="10d047005aabd8a96c7ff5d29ff76ca00a6ba8ff",
    test="22cde5d4b9ac43ac73f1309cb1021f0dd187e9f0", 
    golden="22cde5d4b9ac43ac73f1309cb1021f0dd187e9f0",
)
def transmission_22cde5d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="10d047005aabd8a96c7ff5d29ff76ca00a6ba8ff",
            test="22cde5d4b9ac43ac73f1309cb1021f0dd187e9f0", 
            golden="22cde5d4b9ac43ac73f1309cb1021f0dd187e9f0",
            jest_test_files=["gtk/Application.cc", "gtk/DetailsDialog.cc", "gtk/Session.cc", "gtk/Session.h", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/rpcimpl.h", "qt/RpcClient.cc", "qt/RpcClient.h", "tests/libtransmission/rpc-test.cc"], 
        )
    ])

@problem(
    id="transmission-10d0470",
    description="""
    refactor: convert `tr_incomplete_metadata` to c++ class (#6383)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="5000edef0191e5dc4ea5b8dec37da11510a08c16",
    test="10d047005aabd8a96c7ff5d29ff76ca00a6ba8ff", 
    golden="10d047005aabd8a96c7ff5d29ff76ca00a6ba8ff",
)
def transmission_10d0470(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="5000edef0191e5dc4ea5b8dec37da11510a08c16",
            test="10d047005aabd8a96c7ff5d29ff76ca00a6ba8ff", 
            golden="10d047005aabd8a96c7ff5d29ff76ca00a6ba8ff",
            jest_test_files=["libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/torrent-magnet.cc", "libtransmission/torrent-magnet.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/torrent-magnet-test.cc"], 
        )
    ])

@problem(
    id="transmission-5e51fda",
    description="""
    refactor: remove tr_strlcpy() (#6433)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="0ef34878de670f068091fb2ed51556a1467ba383",
    test="5e51fda92e9d3103678ac6947f99465b23795fcb", 
    golden="5e51fda92e9d3103678ac6947f99465b23795fcb",
)
def transmission_5e51fda(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="0ef34878de670f068091fb2ed51556a1467ba383",
            test="5e51fda92e9d3103678ac6947f99465b23795fcb", 
            golden="5e51fda92e9d3103678ac6947f99465b23795fcb",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "libtransmission/announcer.cc", "libtransmission/rpc-server.cc", "libtransmission/utils.cc", "libtransmission/utils.h", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-45298e5",
    description="""
    fix: don't create all 0-byte files in `MakemetaTest::makeRandomFiles()` (#6394)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="bfa5da9705faedcf72799841e48b37675652e478",
    test="45298e5a4e38b43c146735d4b44d5aba50ffa033", 
    golden="45298e5a4e38b43c146735d4b44d5aba50ffa033",
)
def transmission_45298e5(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="bfa5da9705faedcf72799841e48b37675652e478",
            test="45298e5a4e38b43c146735d4b44d5aba50ffa033", 
            golden="45298e5a4e38b43c146735d4b44d5aba50ffa033",
            jest_test_files=["tests/libtransmission/makemeta-test.cc"], 
        )
    ])

@problem(
    id="transmission-581d9c3",
    description="""
    fix: gcc-13 warnings pt. 2 (#6404)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="a9fa9430ba2566c6dc3a44129fea556b32c301c4",
    test="581d9c34cc244d6b9a8f6b08cf0629ddb3a22a6f", 
    golden="581d9c34cc244d6b9a8f6b08cf0629ddb3a22a6f",
)
def transmission_581d9c3(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="a9fa9430ba2566c6dc3a44129fea556b32c301c4",
            test="581d9c34cc244d6b9a8f6b08cf0629ddb3a22a6f", 
            golden="581d9c34cc244d6b9a8f6b08cf0629ddb3a22a6f",
            jest_test_files=["gtk/FileList.cc", "gtk/OptionsDialog.cc", "libtransmission/net.h", "libtransmission/resume.cc", "libtransmission/subprocess-posix.cc", "libtransmission/transmission.h", "macosx/FilePriorityCell.mm", "tests/gtest/CMakeLists.txt", "tests/libtransmission/net-test.cc"], 
        )
    ])

@problem(
    id="transmission-a494da4",
    description="""
    fix: fill random buffer in chunks with mbedtls crypto backend (#6379)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="33c4cd1c44da1d1979d448fe71480a60e302db82",
    test="a494da4fea1b45a41fb2012a69dc4c9c0087be97", 
    golden="a494da4fea1b45a41fb2012a69dc4c9c0087be97",
)
def transmission_a494da4(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="33c4cd1c44da1d1979d448fe71480a60e302db82",
            test="a494da4fea1b45a41fb2012a69dc4c9c0087be97", 
            golden="a494da4fea1b45a41fb2012a69dc4c9c0087be97",
            jest_test_files=["libtransmission/crypto-utils-mbedtls.cc", "tests/libtransmission/crypto-test.cc"], 
        )
    ])

@problem(
    id="transmission-5683751",
    description="""
    refactor: tr_block_info cleanup (#6342)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="3cd66899fe5c8434aef71e179024cf6eaa0d5691",
    test="56837517b0f99031a1df1afab9d0803d51cd2d78", 
    golden="56837517b0f99031a1df1afab9d0803d51cd2d78",
)
def transmission_5683751(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="3cd66899fe5c8434aef71e179024cf6eaa0d5691",
            test="56837517b0f99031a1df1afab9d0803d51cd2d78", 
            golden="56837517b0f99031a1df1afab9d0803d51cd2d78",
            jest_test_files=["libtransmission/block-info.cc", "libtransmission/block-info.h", "libtransmission/file-piece-map.cc", "libtransmission/file-piece-map.h", "libtransmission/resume.cc", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent.cc", "libtransmission/torrent.h", "tests/libtransmission/block-info-test.cc", "tests/libtransmission/file-piece-map-test.cc"], 
        )
    ])

@problem(
    id="transmission-2e46bad",
    description="""
    refactor: constify the inout module (#6328)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="9e7a860b5709b532bc08d797f82958016b008b82",
    test="2e46bad22d9e7c716a5cc3e9cba849356b0b4bca", 
    golden="2e46bad22d9e7c716a5cc3e9cba849356b0b4bca",
)
def transmission_2e46bad(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="9e7a860b5709b532bc08d797f82958016b008b82",
            test="2e46bad22d9e7c716a5cc3e9cba849356b0b4bca", 
            golden="2e46bad22d9e7c716a5cc3e9cba849356b0b4bca",
            jest_test_files=["libtransmission/cache.cc", "libtransmission/cache.h", "libtransmission/inout.cc", "libtransmission/inout.h", "libtransmission/open-files.cc", "libtransmission/open-files.h", "libtransmission/peer-msgs.cc", "libtransmission/session-settings.h", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/transmission.h", "libtransmission/variant-converters.cc", "tests/libtransmission/open-files-test.cc", "tests/libtransmission/settings-test.cc"], 
        )
    ])

@problem(
    id="transmission-64d9d57",
    description="""
    chore: fix minor clang-tidy warnings (#6275)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="65d8ae53577428c07c9740f38dcce6d4b97adbef",
    test="64d9d573637e4a2212e7b0f09720af6e5784d21b", 
    golden="64d9d573637e4a2212e7b0f09720af6e5784d21b",
)
def transmission_64d9d57(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="65d8ae53577428c07c9740f38dcce6d4b97adbef",
            test="64d9d573637e4a2212e7b0f09720af6e5784d21b", 
            golden="64d9d573637e4a2212e7b0f09720af6e5784d21b",
            jest_test_files=["gtk/Actions.cc", "gtk/Application.cc", "gtk/IconCache.cc", "libtransmission/announcer-http.cc", "libtransmission/announcer-udp.cc", "libtransmission/announcer.cc", "libtransmission/bandwidth.cc", "libtransmission/bandwidth.h", "libtransmission/bitfield.cc", "libtransmission/block-info.cc", "libtransmission/blocklist.cc", "libtransmission/cache.cc", "libtransmission/clients.cc", "libtransmission/completion.cc", "libtransmission/crypto-utils-openssl.cc", "libtransmission/crypto-utils.cc", "libtransmission/file-piece-map.cc", "libtransmission/file-piece-map.h", "libtransmission/global-ip-cache.cc", "libtransmission/handshake.cc", "libtransmission/inout.cc", "libtransmission/log.cc", "libtransmission/magnet-metainfo.cc", "libtransmission/net.cc", "libtransmission/peer-mgr.cc", "libtransmission/peer-mse.cc", "libtransmission/peer-msgs.cc", "libtransmission/peer-socket.cc", "libtransmission/platform.cc", "libtransmission/port-forwarding-upnp.cc", "libtransmission/quark.cc", "libtransmission/resume.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/session-alt-speeds.cc", "libtransmission/session-id.cc", "libtransmission/session-settings.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/subprocess-posix.cc", "libtransmission/torrent-files.cc", "libtransmission/torrent-magnet.cc", "libtransmission/torrent-metainfo.cc", "libtransmission/torrents.cc", "libtransmission/tr-dht.cc", "libtransmission/tr-getopt.cc", "libtransmission/tr-lpd.cc", "libtransmission/tr-udp.cc", "libtransmission/tr-utp.cc", "libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/values.h", "libtransmission/variant-benc.cc", "libtransmission/variant-json.cc", "libtransmission/variant.cc", "libtransmission/verify.cc", "libtransmission/watchdir-inotify.cc", "libtransmission/watchdir-win32.cc", "libtransmission/web-utils.cc", "libtransmission/web.cc", "libtransmission/webseed.cc", "qt/AboutDialog.cc", "qt/AddData.cc", "qt/Application.cc", "qt/BaseDialog.h", "qt/ComInteropHelper.cc", "qt/DBusInteropHelper.cc", "qt/DetailsDialog.cc", "qt/DetailsDialog.h", "qt/FileTreeItem.h", "qt/FileTreeModel.cc", "qt/FileTreeView.cc", "qt/FilterBar.cc", "qt/FilterBarComboBox.cc", "qt/FilterBarComboBoxDelegate.cc", "qt/Filters.h", "qt/FreeSpaceLabel.cc", "qt/IconCache.cc", "qt/IconToolButton.cc", "qt/InteropObject.cc", "qt/LicenseDialog.cc", "qt/MainWindow.cc", "qt/MakeDialog.cc", "qt/OptionsDialog.cc", "qt/PathButton.cc", "qt/Prefs.cc", "qt/PrefsDialog.cc", "qt/RpcClient.cc", "qt/RpcQueue.cc", "qt/Session.cc", "qt/Torrent.cc", "qt/TorrentDelegate.cc", "qt/TorrentDelegateMin.cc", "qt/TorrentDelegateMin.h", "qt/TorrentFilter.cc", "qt/TorrentModel.cc", "qt/TorrentView.cc", "qt/TrackerDelegate.cc", "qt/TrackerDelegate.h", "qt/TrackerModel.cc", "qt/TrackerModelFilter.cc", "qt/VariantHelpers.cc", "qt/WatchDir.cc", "tests/libtransmission/announcer-test.cc", "tests/libtransmission/benc-test.cc", "tests/libtransmission/buffer-test.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/global-ip-cache-test.cc", "tests/libtransmission/handshake-test.cc", "tests/libtransmission/move-test.cc", "tests/libtransmission/strbuf-test.cc", "tests/libtransmission/torrent-metainfo-test.cc", "tests/libtransmission/values-test.cc", "tests/libtransmission/variant-test.cc"], 
        )
    ])

@problem(
    id="transmission-36f33c0",
    description="""
    fix: recent clang-tidy warnings (#6233)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="a2e97234d245ec54b116c3f1d548c6f0aff597e1",
    test="36f33c0d3036647c3c036b5000fcc538f536ab54", 
    golden="36f33c0d3036647c3c036b5000fcc538f536ab54",
)
def transmission_36f33c0(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="a2e97234d245ec54b116c3f1d548c6f0aff597e1",
            test="36f33c0d3036647c3c036b5000fcc538f536ab54", 
            golden="36f33c0d3036647c3c036b5000fcc538f536ab54",
            jest_test_files=["libtransmission/peer-mgr.cc", "tests/libtransmission/file-piece-map-test.cc"], 
        )
    ])

@problem(
    id="transmission-a952a07",
    description="""
    refactor: remove the tr_error** idiom (#6198)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="4d95aa529815eecab0697510731863d3bfb95f44",
    test="a952a0731f9fc1251197fcfcef5339df56c973ab", 
    golden="a952a0731f9fc1251197fcfcef5339df56c973ab",
)
def transmission_a952a07(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="4d95aa529815eecab0697510731863d3bfb95f44",
            test="a952a0731f9fc1251197fcfcef5339df56c973ab", 
            golden="a952a0731f9fc1251197fcfcef5339df56c973ab",
            jest_test_files=["cli/cli.cc", "daemon/daemon-posix.cc", "daemon/daemon-win32.cc", "daemon/daemon.cc", "daemon/daemon.h", "gtk/MakeDialog.cc", "gtk/Session.cc", "gtk/Utils.cc", "gtk/Utils.h", "libtransmission/announce-list.cc", "libtransmission/announce-list.h", "libtransmission/announcer-http.cc", "libtransmission/benc.h", "libtransmission/blocklist.cc", "libtransmission/error.cc", "libtransmission/error.h", "libtransmission/file-capacity.cc", "libtransmission/file-posix.cc", "libtransmission/file-win32.cc", "libtransmission/file.cc", "libtransmission/file.h", "libtransmission/handshake.cc", "libtransmission/inout.cc", "libtransmission/magnet-metainfo.cc", "libtransmission/magnet-metainfo.h", "libtransmission/makemeta.cc", "libtransmission/makemeta.h", "libtransmission/open-files.cc", "libtransmission/peer-io.cc", "libtransmission/peer-socket.cc", "libtransmission/peer-socket.h", "libtransmission/resume.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/session-id.cc", "libtransmission/subprocess-posix.cc", "libtransmission/subprocess-win32.cc", "libtransmission/subprocess.h", "libtransmission/torrent-ctor.cc", "libtransmission/torrent-files.cc", "libtransmission/torrent-files.h", "libtransmission/torrent-magnet.cc", "libtransmission/torrent-magnet.h", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent-metainfo.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/tr-buffer.h", "libtransmission/transmission.h", "libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/variant-json.cc", "libtransmission/variant.cc", "libtransmission/variant.h", "libtransmission/watchdir.cc", "macosx/CreatorWindowController.mm", "macosx/Torrent.mm", "qt/MakeDialog.cc", "tests/libtransmission/announce-list-test.cc", "tests/libtransmission/benc-test.cc", "tests/libtransmission/copy-test.cc", "tests/libtransmission/error-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/open-files-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/subprocess-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/torrent-magnet-test.cc", "tests/libtransmission/torrent-metainfo-test.cc", "tests/libtransmission/utils-test.cc", "tests/libtransmission/variant-test.cc", "utils/create.cc", "utils/edit.cc", "utils/show.cc"], 
        )
    ])

@problem(
    id="transmission-424a9b5",
    description="""
    chore: cleanup timespans in remaining headers (#6199)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="2e7448c9bcc17b722ea26a209fb5b2ab86a0554c",
    test="424a9b5e17998d201948ab916e83f5d68d6d997f", 
    golden="424a9b5e17998d201948ab916e83f5d68d6d997f",
)
def transmission_424a9b5(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="2e7448c9bcc17b722ea26a209fb5b2ab86a0554c",
            test="424a9b5e17998d201948ab916e83f5d68d6d997f", 
            golden="424a9b5e17998d201948ab916e83f5d68d6d997f",
            jest_test_files=["gtk/DynamicPropertyStore.h", "libtransmission/favicon-cache.h", "libtransmission/global-ip-cache.cc", "libtransmission/global-ip-cache.h", "libtransmission/observable.h", "libtransmission/tr-lpd.cc", "libtransmission/utils.mm", "macosx/DefaultAppHelper.h", "macosx/DefaultAppHelper.mm", "macosx/GroupCell.h", "macosx/GroupCell.mm", "macosx/ProgressBarView.h", "macosx/ProgressBarView.mm", "macosx/SmallTorrentCell.h", "macosx/SmallTorrentCell.mm", "macosx/TorrentCellActionButton.h", "macosx/TorrentCellActionButton.mm", "macosx/TorrentCellControlButton.h", "macosx/TorrentCellControlButton.mm", "macosx/TorrentCellRevealButton.h", "macosx/TorrentCellRevealButton.mm", "macosx/VDKQueue/VDKQueue.h", "macosx/VDKQueue/VDKQueue.mm", "tests/libtransmission/global-ip-cache-test.cc", "tests/libtransmission/tr-peer-info-test.cc", "web/src/force-verify-dialog.js"], 
        )
    ])

@problem(
    id="transmission-2e7448c",
    description="""
    fix: appendSanitizedComponent is too aggressive on non-WIN32 (and not enough aggressive on WIN32) (#6187)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1b5322685342e44fc7a1caa2b3f83cea25d073a4",
    test="2e7448c9bcc17b722ea26a209fb5b2ab86a0554c", 
    golden="2e7448c9bcc17b722ea26a209fb5b2ab86a0554c",
)
def transmission_2e7448c(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1b5322685342e44fc7a1caa2b3f83cea25d073a4",
            test="2e7448c9bcc17b722ea26a209fb5b2ab86a0554c", 
            golden="2e7448c9bcc17b722ea26a209fb5b2ab86a0554c",
            jest_test_files=["libtransmission/torrent-files.cc", "tests/libtransmission/torrent-files-test.cc"], 
        )
    ])

@problem(
    id="transmission-1c421d6",
    description="""
    Minor CMake maintainability improvements (#6186)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c697d95ad352be74638169fac8280bada8b4c54b",
    test="1c421d6d23044398c69e4b8965d7ca30c2189ec3", 
    golden="1c421d6d23044398c69e4b8965d7ca30c2189ec3",
)
def transmission_1c421d6(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c697d95ad352be74638169fac8280bada8b4c54b",
            test="1c421d6d23044398c69e4b8965d7ca30c2189ec3", 
            golden="1c421d6d23044398c69e4b8965d7ca30c2189ec3",
            jest_test_files=[".gitmodules", "CMakeLists.txt", "cmake/FindFastFloat.cmake", "cmake/FindFmt.cmake", "cmake/FindRapidJSON.cmake", "cmake/FindSmall.cmake", "cmake/FindUtfCpp.cmake", "cmake/FindWideInteger.cmake", "cmake/TrMacros.cmake", "dist/msi/CMakeLists.txt", "macosx/CMakeLists.txt", "macosx/QuickLookPlugin/CMakeLists.txt", "macosx/VDKQueue/CMakeLists.txt", "tests/gtest/CMakeLists.txt", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/subprocess-test-program.cc", "third-party/rapavlik-cmake-modules", "third-party/rpavlik-cmake-modules"], 
        )
    ])

@problem(
    id="transmission-c697d95",
    description="""
    fix: crash after nullptr dereference in rpcimpl (#6177)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="ccce37ba6c0538511f825308f56fa6f40ab98abd",
    test="c697d95ad352be74638169fac8280bada8b4c54b", 
    golden="c697d95ad352be74638169fac8280bada8b4c54b",
)
def transmission_c697d95(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="ccce37ba6c0538511f825308f56fa6f40ab98abd",
            test="c697d95ad352be74638169fac8280bada8b4c54b", 
            golden="c697d95ad352be74638169fac8280bada8b4c54b",
            jest_test_files=["libtransmission/rpcimpl.cc", "tests/libtransmission/rpc-test.cc"], 
        )
    ])

@problem(
    id="transmission-eb58996",
    description="""
    chore: remove unused tr_announce_list::announce_to_scrape(tr_quark) (#6157)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="6d958bd5fc2b43983b9475d3af3e434a2153081e",
    test="eb58996c9fde36e33e96197a6410227f99084c24", 
    golden="eb58996c9fde36e33e96197a6410227f99084c24",
)
def transmission_eb58996(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="6d958bd5fc2b43983b9475d3af3e434a2153081e",
            test="eb58996c9fde36e33e96197a6410227f99084c24", 
            golden="eb58996c9fde36e33e96197a6410227f99084c24",
            jest_test_files=["libtransmission/announce-list.cc", "libtransmission/announce-list.h", "tests/libtransmission/announce-list-test.cc"], 
        )
    ])

@problem(
    id="transmission-0259edb",
    description="""
    fix: json string serializer improperly escaping characters (#6005)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d273e0f90ec5dff09b4c82d1ab20a9fe7018d26c",
    test="0259edbaf3996e33dbd3b85faa8c0254a47586f0", 
    golden="0259edbaf3996e33dbd3b85faa8c0254a47586f0",
)
def transmission_0259edb(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d273e0f90ec5dff09b4c82d1ab20a9fe7018d26c",
            test="0259edbaf3996e33dbd3b85faa8c0254a47586f0", 
            golden="0259edbaf3996e33dbd3b85faa8c0254a47586f0",
            jest_test_files=["libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/variant-json.cc", "tests/libtransmission/json-test.cc"], 
        )
    ])

@problem(
    id="transmission-fbfbfac",
    description="""
    fix: minor coverity warnings (#5916)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="59c638c63dea7b7c78a9c36a5cdec51fa3aa2a79",
    test="fbfbfac3ae3216b3f0f239b140e5f5cb22533449", 
    golden="fbfbfac3ae3216b3f0f239b140e5f5cb22533449",
)
def transmission_fbfbfac(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="59c638c63dea7b7c78a9c36a5cdec51fa3aa2a79",
            test="fbfbfac3ae3216b3f0f239b140e5f5cb22533449", 
            golden="fbfbfac3ae3216b3f0f239b140e5f5cb22533449",
            jest_test_files=["gtk/Application.cc", "gtk/FilterBar.cc", "gtk/Utils.h", "libtransmission/announcer.cc", "libtransmission/file-capacity.cc", "libtransmission/session.cc", "libtransmission/tr-udp.cc", "libtransmission/utils.h", "tests/libtransmission/announce-list-test.cc", "tests/libtransmission/file-test.cc", "utils/remote.cc"], 
        )
    ])

@problem(
    id="transmission-449549c",
    description="""
    fix: do not mark peer as not connectable when we are currently connected (#5889)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="916534a687af9f6d98a9dbf6ac748dde4489866c",
    test="449549c84f7482db5054fc0080fa2f8be8af0729", 
    golden="449549c84f7482db5054fc0080fa2f8be8af0729",
)
def transmission_449549c(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="916534a687af9f6d98a9dbf6ac748dde4489866c",
            test="449549c84f7482db5054fc0080fa2f8be8af0729", 
            golden="449549c84f7482db5054fc0080fa2f8be8af0729",
            jest_test_files=["libtransmission/peer-mgr.cc", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/tr-peer-info-test.cc"], 
        )
    ])

@problem(
    id="transmission-8873f2a",
    description="""
    fix: announce with query replace bug (#5871)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1a86c65b44f04af6964fa24f5ac47e62f05a4788",
    test="8873f2a50c1387bf4b6e47b01faa4bab5f4254b8", 
    golden="8873f2a50c1387bf4b6e47b01faa4bab5f4254b8",
)
def transmission_8873f2a(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1a86c65b44f04af6964fa24f5ac47e62f05a4788",
            test="8873f2a50c1387bf4b6e47b01faa4bab5f4254b8", 
            golden="8873f2a50c1387bf4b6e47b01faa4bab5f4254b8",
            jest_test_files=["libtransmission/announce-list.cc", "libtransmission/announce-list.h", "tests/libtransmission/announce-list-test.cc"], 
        )
    ])

@problem(
    id="transmission-27f3a5b",
    description="""
    fix: announce LDP on listening interface (#5875)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="586cff9506487eabf72baa3c1588e623a8b1ac63",
    test="27f3a5b82a0456ce7f26f215c4d803f5793a39d8", 
    golden="27f3a5b82a0456ce7f26f215c4d803f5793a39d8",
)
def transmission_27f3a5b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="586cff9506487eabf72baa3c1588e623a8b1ac63",
            test="27f3a5b82a0456ce7f26f215c4d803f5793a39d8", 
            golden="27f3a5b82a0456ce7f26f215c4d803f5793a39d8",
            jest_test_files=["libtransmission/session.h", "libtransmission/tr-lpd.cc", "libtransmission/tr-lpd.h", "tests/libtransmission/lpd-test.cc"], 
        )
    ])

@problem(
    id="transmission-97da2ad",
    description="""
    fix: spelling mistake in `net.h` function call (#5739)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="0f85c9e0e4993f02f91f852a7255049d3853bb1f",
    test="97da2adbca0eca2e6b7a6e83e6d398e9dd69e61c", 
    golden="97da2adbca0eca2e6b7a6e83e6d398e9dd69e61c",
)
def transmission_97da2ad(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="0f85c9e0e4993f02f91f852a7255049d3853bb1f",
            test="97da2adbca0eca2e6b7a6e83e6d398e9dd69e61c", 
            golden="97da2adbca0eca2e6b7a6e83e6d398e9dd69e61c",
            jest_test_files=["libtransmission/net.h", "tests/libtransmission/net-test.cc"], 
        )
    ])

@problem(
    id="transmission-2211086",
    description="""
    fix: conform to libcurl requirements to avoid memory leak (#5702)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f83a60830ae280c64789ea5647fd408a4224b7ce",
    test="2211086338e4c7a31026e682448784b14ed61e52", 
    golden="2211086338e4c7a31026e682448784b14ed61e52",
)
def transmission_2211086(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f83a60830ae280c64789ea5647fd408a4224b7ce",
            test="2211086338e4c7a31026e682448784b14ed61e52", 
            golden="2211086338e4c7a31026e682448784b14ed61e52",
            jest_test_files=["cli/cli.cc", "daemon/daemon.cc", "gtk/main.cc", "libtransmission/session-thread.cc", "libtransmission/tr-lpd.cc", "libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/watchdir-win32.cc", "libtransmission/web.cc", "macosx/main.mm", "qt/Application.cc", "tests/libtransmission/announcer-udp-test.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/watchdir-test.cc", "utils/remote.cc", "utils/show.cc"], 
        )
    ])

@problem(
    id="transmission-9c17463",
    description="""
    fix: revert 'perf: improve IPv4 `tr_address` comparison' (#5709)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="0fbafc9e18383ccbb27963f4bba173c66743f286",
    test="9c17463a80d8127537c6cfaf7f323e58083209c1", 
    golden="9c17463a80d8127537c6cfaf7f323e58083209c1",
)
def transmission_9c17463(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="0fbafc9e18383ccbb27963f4bba173c66743f286",
            test="9c17463a80d8127537c6cfaf7f323e58083209c1", 
            golden="9c17463a80d8127537c6cfaf7f323e58083209c1",
            jest_test_files=["libtransmission/net.cc", "tests/libtransmission/net-test.cc"], 
        )
    ])

@problem(
    id="transmission-6426168",
    description="""
    fix: use both address + port together as a key for peer lookup (#5619)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="4b9b9920bfea51a9fe0f2a9ac69c22db3571be85",
    test="64261685d8d474ee378a9dbaf3c2ee07761be342", 
    golden="64261685d8d474ee378a9dbaf3c2ee07761be342",
)
def transmission_6426168(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="4b9b9920bfea51a9fe0f2a9ac69c22db3571be85",
            test="64261685d8d474ee378a9dbaf3c2ee07761be342", 
            golden="64261685d8d474ee378a9dbaf3c2ee07761be342",
            jest_test_files=["code_style.sh", "libtransmission/handshake.cc", "libtransmission/handshake.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-mgr.h", "libtransmission/peer-msgs.cc", "tests/libtransmission/handshake-test.cc"], 
        )
    ])

@problem(
    id="transmission-ddac059",
    description="""
    fix: return error when renaming into existing file (#5563)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b8ff35c4ce93cb12df20961f8477cc34c8362241",
    test="ddac05954b046b55f4bf25f45204f83f8ad8da4b", 
    golden="ddac05954b046b55f4bf25f45204f83f8ad8da4b",
)
def transmission_ddac059(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b8ff35c4ce93cb12df20961f8477cc34c8362241",
            test="ddac05954b046b55f4bf25f45204f83f8ad8da4b", 
            golden="ddac05954b046b55f4bf25f45204f83f8ad8da4b",
            jest_test_files=["libtransmission/torrent.cc", "tests/libtransmission/rename-test.cc"], 
        )
    ])

@problem(
    id="transmission-802619e",
    description="""
    fix: fixes and improvements to global IP query (#5510)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c8e84f870b5c707d712831525cc0910a907ac0ef",
    test="802619e174fd746d95ca8d302a93eec92fe4e112", 
    golden="802619e174fd746d95ca8d302a93eec92fe4e112",
)
def transmission_802619e(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c8e84f870b5c707d712831525cc0910a907ac0ef",
            test="802619e174fd746d95ca8d302a93eec92fe4e112", 
            golden="802619e174fd746d95ca8d302a93eec92fe4e112",
            jest_test_files=["libtransmission/global-ip-cache.cc", "libtransmission/global-ip-cache.h", "libtransmission/session.cc", "libtransmission/session.h", "tests/libtransmission/global-ip-cache-test.cc"], 
        )
    ])

@problem(
    id="transmission-2cf9678",
    description="""
    fix: revert buffer reserve space (#5528)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="e88bf946e1cfa90323c8f07ef7e3dc0fdff6dacb",
    test="2cf96787377d762ffd6098c5143886b229a739aa", 
    golden="2cf96787377d762ffd6098c5143886b229a739aa",
)
def transmission_2cf9678(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="e88bf946e1cfa90323c8f07ef7e3dc0fdff6dacb",
            test="2cf96787377d762ffd6098c5143886b229a739aa", 
            golden="2cf96787377d762ffd6098c5143886b229a739aa",
            jest_test_files=["libtransmission/announcer-udp.cc", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "libtransmission/peer-mse.h", "libtransmission/peer-msgs.cc", "libtransmission/peer-socket.cc", "libtransmission/peer-socket.h", "libtransmission/tr-buffer.h", "libtransmission/variant-benc.cc", "libtransmission/variant-json.cc", "libtransmission/variant.cc", "tests/libtransmission/announcer-udp-test.cc", "tests/libtransmission/buffer-test.cc"], 
        )
    ])

@problem(
    id="transmission-ea500ec",
    description="""
    fixup! feat: add global IP cache, fix UDP connection failure warnings (#5506)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="cb6358048db10e77280e8dd820d52ed9c8213cff",
    test="ea500ecdcdb4df6a03db55f75cd47d38fad5f14b", 
    golden="ea500ecdcdb4df6a03db55f75cd47d38fad5f14b",
)
def transmission_ea500ec(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="cb6358048db10e77280e8dd820d52ed9c8213cff",
            test="ea500ecdcdb4df6a03db55f75cd47d38fad5f14b", 
            golden="ea500ecdcdb4df6a03db55f75cd47d38fad5f14b",
            jest_test_files=["tests/libtransmission/global-ip-cache-test.cc"], 
        )
    ])

@problem(
    id="transmission-474a30a",
    description="""
    feat: add global IP cache, fix UDP connection failure warnings
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="bd8b50ef7b5e5fc030e2947c4ca46f3ca642c299",
    test="474a30ab2dcadd909f076c24407481cd4d07e60e", 
    golden="474a30ab2dcadd909f076c24407481cd4d07e60e",
)
def transmission_474a30a(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="bd8b50ef7b5e5fc030e2947c4ca46f3ca642c299",
            test="474a30ab2dcadd909f076c24407481cd4d07e60e", 
            golden="474a30ab2dcadd909f076c24407481cd4d07e60e",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "docs/Editing-Configuration-Files.md", "libtransmission/CMakeLists.txt", "libtransmission/announcer.cc", "libtransmission/global-ip-cache.cc", "libtransmission/global-ip-cache.h", "libtransmission/net.cc", "libtransmission/net.h", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/tr-udp.cc", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/global-ip-cache-test.cc", "tests/libtransmission/net-test.cc"], 
        )
    ])

@problem(
    id="transmission-2999e71",
    description="""
    fix: typos in libtransmission tests (#5468)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f34b1e624c53cdac9aa2bbf694e356d2d069d940",
    test="2999e71e765ded8dcde2df175e4da2ce7eaa49ca", 
    golden="2999e71e765ded8dcde2df175e4da2ce7eaa49ca",
)
def transmission_2999e71(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f34b1e624c53cdac9aa2bbf694e356d2d069d940",
            test="2999e71e765ded8dcde2df175e4da2ce7eaa49ca", 
            golden="2999e71e765ded8dcde2df175e4da2ce7eaa49ca",
            jest_test_files=["tests/libtransmission/announcer-udp-test.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/session-alt-speeds-test.cc", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-e8fcb02",
    description="""
    fix: use user-preferred locale (#5444)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c2002c9481b7090e8cebdf960630d1a42215fc09",
    test="e8fcb025a06eca6923f00228c3318501fbb93263", 
    golden="e8fcb025a06eca6923f00228c3318501fbb93263",
)
def transmission_e8fcb02(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c2002c9481b7090e8cebdf960630d1a42215fc09",
            test="e8fcb025a06eca6923f00228c3318501fbb93263", 
            golden="e8fcb025a06eca6923f00228c3318501fbb93263",
            jest_test_files=["cli/cli.cc", "daemon/daemon.cc", "gtk/main.cc", "libtransmission/utils.cc", "libtransmission/utils.h", "macosx/main.mm", "qt/Application.cc", "tests/libtransmission/json-test.cc", "tests/utils/run_transmission_show.cmake", "utils/create.cc", "utils/edit.cc", "utils/remote.cc", "utils/show.cc"], 
        )
    ])

@problem(
    id="transmission-9f8a7a6",
    description="""
    fix: Buffer::Buffer(Buffer&&) bug  (#5435)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f9178eb084acc624320f2de26c16a1a7652f55a6",
    test="9f8a7a656eb4fc17156b4dee1843b1ed0bb87341", 
    golden="9f8a7a656eb4fc17156b4dee1843b1ed0bb87341",
)
def transmission_9f8a7a6(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f9178eb084acc624320f2de26c16a1a7652f55a6",
            test="9f8a7a656eb4fc17156b4dee1843b1ed0bb87341", 
            golden="9f8a7a656eb4fc17156b4dee1843b1ed0bb87341",
            jest_test_files=["libtransmission/tr-buffer.h", "tests/libtransmission/buffer-test.cc"], 
        )
    ])

@problem(
    id="transmission-d63165e",
    description="""
    perf: fix wishlist cpu load regression, pt. 2 (#5273)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="25f38d5ff358802ad1d7bfc0dc477b5e5db853e6",
    test="d63165e8a4cbcf98c487d04b7272b87afe108d1d", 
    golden="d63165e8a4cbcf98c487d04b7272b87afe108d1d",
)
def transmission_d63165e(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="25f38d5ff358802ad1d7bfc0dc477b5e5db853e6",
            test="d63165e8a4cbcf98c487d04b7272b87afe108d1d", 
            golden="d63165e8a4cbcf98c487d04b7272b87afe108d1d",
            jest_test_files=["libtransmission/file-piece-map.cc", "libtransmission/file-piece-map.h", "libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-mgr-wishlist.h", "libtransmission/peer-mgr.cc", "tests/libtransmission/peer-mgr-wishlist-test.cc"], 
        )
    ])

@problem(
    id="transmission-c60bb5b",
    description="""
    fix: crash when magnet dn isn't utf-8 (#5244)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="ca44c9143af7361081d000a20b1b986e72dbc3ff",
    test="c60bb5b834f0518a81ca3117a0f2af01fd53850f", 
    golden="c60bb5b834f0518a81ca3117a0f2af01fd53850f",
)
def transmission_c60bb5b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="ca44c9143af7361081d000a20b1b986e72dbc3ff",
            test="c60bb5b834f0518a81ca3117a0f2af01fd53850f", 
            golden="c60bb5b834f0518a81ca3117a0f2af01fd53850f",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "libtransmission/CMakeLists.txt", "libtransmission/magnet-metainfo.h", "libtransmission/torrent-metainfo.cc", "libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/utils.mm", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-033d698",
    description="""
    fix: parsing of ipv6 tracker announce URLs (#5174)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="39e3e1d87b69a1a5e63a6cc17ef62c3b40034711",
    test="033d69830611e0f948e35e4df2c1ff8664712a91", 
    golden="033d69830611e0f948e35e4df2c1ff8664712a91",
)
def transmission_033d698(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="39e3e1d87b69a1a5e63a6cc17ef62c3b40034711",
            test="033d69830611e0f948e35e4df2c1ff8664712a91", 
            golden="033d69830611e0f948e35e4df2c1ff8664712a91",
            jest_test_files=["libtransmission/web-utils.cc", "tests/libtransmission/web-utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-39e3e1d",
    description="""
    fix: increase priority of first and last piece of each file (#5167)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="2dd39596d1ac99f216c34a201423af36454e9f2a",
    test="39e3e1d87b69a1a5e63a6cc17ef62c3b40034711", 
    golden="39e3e1d87b69a1a5e63a6cc17ef62c3b40034711",
)
def transmission_39e3e1d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="2dd39596d1ac99f216c34a201423af36454e9f2a",
            test="39e3e1d87b69a1a5e63a6cc17ef62c3b40034711", 
            golden="39e3e1d87b69a1a5e63a6cc17ef62c3b40034711",
            jest_test_files=["libtransmission/file-piece-map.cc", "libtransmission/file-piece-map.h", "tests/libtransmission/file-piece-map-test.cc"], 
        )
    ])

@problem(
    id="transmission-848212e",
    description="""
    fix: escaped representation of non-BMP characters when generating JSON (#5096)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="8fc904617bffc36127b90989093d5686701a4d23",
    test="848212eea11da1a989734c2b09d8ac13f5a8030f", 
    golden="848212eea11da1a989734c2b09d8ac13f5a8030f",
)
def transmission_848212e(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="8fc904617bffc36127b90989093d5686701a4d23",
            test="848212eea11da1a989734c2b09d8ac13f5a8030f", 
            golden="848212eea11da1a989734c2b09d8ac13f5a8030f",
            jest_test_files=["libtransmission/variant-json.cc", "tests/libtransmission/json-test.cc"], 
        )
    ])

@problem(
    id="transmission-d327350",
    description="""
    fix: 5053 old torrent files keep appearing (#5117)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d21a3b622a26d5adc9dcefe70fc8f695d6a886e2",
    test="d3273504bdbc19466fd5ca4254d3080510c75df6", 
    golden="d3273504bdbc19466fd5ca4254d3080510c75df6",
)
def transmission_d327350(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d21a3b622a26d5adc9dcefe70fc8f695d6a886e2",
            test="d3273504bdbc19466fd5ca4254d3080510c75df6", 
            golden="d3273504bdbc19466fd5ca4254d3080510c75df6",
            jest_test_files=["libtransmission/resume.cc", "libtransmission/resume.h", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent.cc", "tests/libtransmission/rename-test.cc"], 
        )
    ])

@problem(
    id="transmission-211e3fc",
    description="""
    fix: always add `announce` key even when including announce-list (#5106)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="03a23cf797bab9b6ce8ad7e2c246046027cfcd74",
    test="211e3fc98571f3b55d17b1ff38facdc02762e3ad", 
    golden="211e3fc98571f3b55d17b1ff38facdc02762e3ad",
)
def transmission_211e3fc(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="03a23cf797bab9b6ce8ad7e2c246046027cfcd74",
            test="211e3fc98571f3b55d17b1ff38facdc02762e3ad", 
            golden="211e3fc98571f3b55d17b1ff38facdc02762e3ad",
            jest_test_files=["libtransmission/makemeta.cc", "tests/libtransmission/makemeta-test.cc"], 
        )
    ])

@problem(
    id="transmission-4461aa6",
    description="""
    fix: handle block fragments that arrive from peers out-of-order (#4890)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="9d91d1e96911109eec41ab9d0f942cd7950d2568",
    test="4461aa68d909968d6fc20b7743aa435edec14995", 
    golden="4461aa68d909968d6fc20b7743aa435edec14995",
)
def transmission_4461aa6(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="9d91d1e96911109eec41ab9d0f942cd7950d2568",
            test="4461aa68d909968d6fc20b7743aa435edec14995", 
            golden="4461aa68d909968d6fc20b7743aa435edec14995",
            jest_test_files=["libtransmission/cache.cc", "libtransmission/cache.h", "libtransmission/peer-msgs.cc", "libtransmission/torrent.cc", "libtransmission/webseed.cc", "tests/libtransmission/move-test.cc"], 
        )
    ])

@problem(
    id="transmission-649fd4d",
    description="""
    fix: do not lose magnet links when upgrading from tr3 to 4 (#4840)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="dcd750121118035244529f7ad781f79087377a3b",
    test="649fd4d0d2088a9c38078c9c135ef3d899a9bbae", 
    golden="649fd4d0d2088a9c38078c9c135ef3d899a9bbae",
)
def transmission_649fd4d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="dcd750121118035244529f7ad781f79087377a3b",
            test="649fd4d0d2088a9c38078c9c135ef3d899a9bbae", 
            golden="649fd4d0d2088a9c38078c9c135ef3d899a9bbae",
            jest_test_files=["libtransmission/torrent-metainfo.cc", "libtransmission/torrent-metainfo.h", "tests/libtransmission/assets/gimp-2.10.32-1-arm64.dmg.torrent", "tests/libtransmission/torrent-metainfo-test.cc"], 
        )
    ])

@problem(
    id="transmission-e0753fe",
    description="""
    fix: put 'private' and 'source' inside the metadata 'info' key (#4809)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="065facc07c72ddb7a096cb97b6680d3f13891ddb",
    test="e0753fedb9219e1f3998ed385ec4cbc466dac7ba", 
    golden="e0753fedb9219e1f3998ed385ec4cbc466dac7ba",
)
def transmission_e0753fe(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="065facc07c72ddb7a096cb97b6680d3f13891ddb",
            test="e0753fedb9219e1f3998ed385ec4cbc466dac7ba", 
            golden="e0753fedb9219e1f3998ed385ec4cbc466dac7ba",
            jest_test_files=["libtransmission/makemeta.cc", "tests/libtransmission/makemeta-test.cc"], 
        )
    ])

@problem(
    id="transmission-42a0106",
    description="""
    chore: disable flaky unit tests (#4808)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b64e65cf2eab097d112c28bdf0b16e88f3b36c40",
    test="42a01068c6118b56014c7f63fb777a9e7119fd9a", 
    golden="42a01068c6118b56014c7f63fb777a9e7119fd9a",
)
def transmission_42a0106(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b64e65cf2eab097d112c28bdf0b16e88f3b36c40",
            test="42a01068c6118b56014c7f63fb777a9e7119fd9a", 
            golden="42a01068c6118b56014c7f63fb777a9e7119fd9a",
            jest_test_files=["tests/libtransmission/lpd-test.cc", "tests/libtransmission/timer-test.cc", "tests/libtransmission/watchdir-test.cc"], 
        )
    ])

@problem(
    id="transmission-0e5f7f8",
    description="""
    fix: coverity warnings (#4687)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="724a0f48f04075d3bfd23cea654ba22423fe63fd",
    test="0e5f7f86d7e4e0c70ed5be29abe5296affd1e7fe", 
    golden="0e5f7f86d7e4e0c70ed5be29abe5296affd1e7fe",
)
def transmission_0e5f7f8(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="724a0f48f04075d3bfd23cea654ba22423fe63fd",
            test="0e5f7f86d7e4e0c70ed5be29abe5296affd1e7fe", 
            golden="0e5f7f86d7e4e0c70ed5be29abe5296affd1e7fe",
            jest_test_files=["libtransmission/net.cc", "tests/libtransmission/file-test.cc"], 
        )
    ])

@problem(
    id="transmission-862abe9",
    description="""
    fix: bugprone-unchecked-optional-access warnings in tests (#4672)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="331e1699bc3141e37128e7ee96d3f0ee4dd7840a",
    test="862abe909cc7162581e4bb17b22e05fb1c2775c1", 
    golden="862abe909cc7162581e4bb17b22e05fb1c2775c1",
)
def transmission_862abe9(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="331e1699bc3141e37128e7ee96d3f0ee4dd7840a",
            test="862abe909cc7162581e4bb17b22e05fb1c2775c1", 
            golden="862abe909cc7162581e4bb17b22e05fb1c2775c1",
            jest_test_files=["tests/libtransmission/announcer-test.cc", "tests/libtransmission/announcer-udp-test.cc", "tests/libtransmission/crypto-test.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/handshake-test.cc", "tests/libtransmission/net-test.cc", "tests/libtransmission/open-files-test.cc", "tests/libtransmission/quark-test.cc", "tests/libtransmission/torrent-files-test.cc", "tests/libtransmission/variant-test.cc"], 
        )
    ])

@problem(
    id="transmission-977a190",
    description="""
    fix: msvc warnings (#4651)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="5fe95ad5b0ffe9e53c8bc8dd9082ec67ce9da807",
    test="977a190646785d50ab41b5a171a58aa3fb48bf07", 
    golden="977a190646785d50ab41b5a171a58aa3fb48bf07",
)
def transmission_977a190(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="5fe95ad5b0ffe9e53c8bc8dd9082ec67ce9da807",
            test="977a190646785d50ab41b5a171a58aa3fb48bf07", 
            golden="977a190646785d50ab41b5a171a58aa3fb48bf07",
            jest_test_files=["libtransmission/net.cc", "qt/Application.cc", "qt/FileTreeDelegate.cc", "tests/libtransmission/announcer-udp-test.cc", "utils/remote.cc"], 
        )
    ])

@problem(
    id="transmission-68f6f49",
    description="""
    test: fix a couple of recurring CI flakes in TimerTest
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="bc4acc6814c44acae96bbe01d257de3a79c00eab",
    test="68f6f49c6d3f3c004458d31e29b5d3862298cf67", 
    golden="68f6f49c6d3f3c004458d31e29b5d3862298cf67",
)
def transmission_68f6f49(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="bc4acc6814c44acae96bbe01d257de3a79c00eab",
            test="68f6f49c6d3f3c004458d31e29b5d3862298cf67", 
            golden="68f6f49c6d3f3c004458d31e29b5d3862298cf67",
            jest_test_files=["tests/libtransmission/timer-test.cc"], 
        )
    ])

@problem(
    id="transmission-2b90a5f",
    description="""
    refactor: possible FTBFS fix on arm7 (#4492)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="192a76b62194b7889e01e37db15f0735fc89ba0a",
    test="2b90a5fd55e2eff72f2d41668b39bfae56144f40", 
    golden="2b90a5fd55e2eff72f2d41668b39bfae56144f40",
)
def transmission_2b90a5f(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="192a76b62194b7889e01e37db15f0735fc89ba0a",
            test="2b90a5fd55e2eff72f2d41668b39bfae56144f40", 
            golden="2b90a5fd55e2eff72f2d41668b39bfae56144f40",
            jest_test_files=["libtransmission/crypto-utils.cc", "libtransmission/crypto-utils.h", "tests/libtransmission/crypto-test-ref.h"], 
        )
    ])

@problem(
    id="transmission-9a5d9a0",
    description="""
    refactor: tr_peer_socket (#4325)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="468310300cd535fe8c533f553f111be8501e62db",
    test="9a5d9a0ba2203bee54ec82212c5077210881a6fb", 
    golden="9a5d9a0ba2203bee54ec82212c5077210881a6fb",
)
def transmission_9a5d9a0(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="468310300cd535fe8c533f553f111be8501e62db",
            test="9a5d9a0ba2203bee54ec82212c5077210881a6fb", 
            golden="9a5d9a0ba2203bee54ec82212c5077210881a6fb",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "libtransmission/CMakeLists.txt", "libtransmission/handshake.cc", "libtransmission/net.cc", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/peer-socket.cc", "libtransmission/peer-socket.h", "libtransmission/session.cc", "libtransmission/tr-utp.cc", "tests/libtransmission/handshake-test.cc"], 
        )
    ])

@problem(
    id="transmission-8085ef6",
    description="""
    fix: flaky subprocess tests (#4266)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="af9f1b4e42e9ae71428ae37d68662212a7ace587",
    test="8085ef6acb6412618f69f1f7ad605702e7b9fa9c", 
    golden="8085ef6acb6412618f69f1f7ad605702e7b9fa9c",
)
def transmission_8085ef6(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="af9f1b4e42e9ae71428ae37d68662212a7ace587",
            test="8085ef6acb6412618f69f1f7ad605702e7b9fa9c", 
            golden="8085ef6acb6412618f69f1f7ad605702e7b9fa9c",
            jest_test_files=["tests/libtransmission/subprocess-test.cc"], 
        )
    ])

@problem(
    id="transmission-ec6cb67",
    description="""
    fix GTK client message log window does not restore level selection (#4242)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="feeea2649e127f553d35c0f3efdd414f3350575f",
    test="ec6cb67c5c096127d9c462cb9f1895ef1a5d2246", 
    golden="ec6cb67c5c096127d9c462cb9f1895ef1a5d2246",
)
def transmission_ec6cb67(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="feeea2649e127f553d35c0f3efdd414f3350575f",
            test="ec6cb67c5c096127d9c462cb9f1895ef1a5d2246", 
            golden="ec6cb67c5c096127d9c462cb9f1895ef1a5d2246",
            jest_test_files=["gtk/MessageLogWindow.cc", "libtransmission/session.cc", "libtransmission/variant-converters.cc", "tests/libtransmission/settings-test.cc"], 
        )
    ])

@problem(
    id="transmission-8a35aa0",
    description="""
    refactor: add tr_rand_obj() (#4238)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="342484d14ad9eff97a88da5845d952ed30e7f601",
    test="8a35aa09036edb887b4f8d463e3666af47ba6d29", 
    golden="8a35aa09036edb887b4f8d463e3666af47ba6d29",
)
def transmission_8a35aa0(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="342484d14ad9eff97a88da5845d952ed30e7f601",
            test="8a35aa09036edb887b4f8d463e3666af47ba6d29", 
            golden="8a35aa09036edb887b4f8d463e3666af47ba6d29",
            jest_test_files=["libtransmission/announcer-udp.cc", "libtransmission/announcer.cc", "libtransmission/crypto-utils.cc", "libtransmission/crypto-utils.h", "libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-mse.cc", "libtransmission/rpc-server.cc", "libtransmission/session-id.cc", "libtransmission/tr-dht.cc", "libtransmission/tr-lpd.cc", "tests/libtransmission/announcer-udp-test.cc", "tests/libtransmission/clients-test.cc", "tests/libtransmission/completion-test.cc", "tests/libtransmission/crypto-test-ref.h", "tests/libtransmission/dht-test.cc", "tests/libtransmission/handshake-test.cc", "tests/libtransmission/lpd-test.cc", "tests/libtransmission/magnet-metainfo-test.cc", "tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-554ba06",
    description="""
    fix: coverity warnings, sonarcloud code smells (#4232)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="ead71e8fd30f094fad538b3670e03328beeb37e8",
    test="554ba06ae2f1aa351d9a7da44559e7e312a39366", 
    golden="554ba06ae2f1aa351d9a7da44559e7e312a39366",
)
def transmission_554ba06(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="ead71e8fd30f094fad538b3670e03328beeb37e8",
            test="554ba06ae2f1aa351d9a7da44559e7e312a39366", 
            golden="554ba06ae2f1aa351d9a7da44559e7e312a39366",
            jest_test_files=["gtk/FaviconCache.cc", "gtk/Session.cc", "libtransmission/announcer-http.cc", "libtransmission/handshake.cc", "libtransmission/peer-msgs.cc", "libtransmission/rpc-server.cc", "libtransmission/session.cc", "libtransmission/verify.cc", "libtransmission/verify.h", "qt/FileTreeItem.cc", "tests/libtransmission/file-test.cc"], 
        )
    ])

@problem(
    id="transmission-19bc155",
    description="""
    fix: new sonarcloud, coverity, gcc warnings (#4229)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="6cd6f78a9f4d64aae56d8bb917df5d057c81dfba",
    test="19bc15523f3661e3999741e039ebf0c6cd583d2c", 
    golden="19bc15523f3661e3999741e039ebf0c6cd583d2c",
)
def transmission_19bc155(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="6cd6f78a9f4d64aae56d8bb917df5d057c81dfba",
            test="19bc15523f3661e3999741e039ebf0c6cd583d2c", 
            golden="19bc15523f3661e3999741e039ebf0c6cd583d2c",
            jest_test_files=["gtk/DetailsDialog.cc", "libtransmission/announcer-udp.cc", "libtransmission/announcer.cc", "libtransmission/bandwidth.cc", "libtransmission/peer-mgr.cc", "libtransmission/peer-mse.h", "libtransmission/session.cc", "tests/libtransmission/bitfield-test.cc"], 
        )
    ])

@problem(
    id="transmission-42f26aa",
    description="""
    fix: ftbfs on Windows (#4204)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="a45cc2a79d6551cee2f689e9f3a3d174687d36cb",
    test="42f26aad0b5d05f93b3302abdc59c778788dc5c4", 
    golden="42f26aad0b5d05f93b3302abdc59c778788dc5c4",
)
def transmission_42f26aa(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="a45cc2a79d6551cee2f689e9f3a3d174687d36cb",
            test="42f26aad0b5d05f93b3302abdc59c778788dc5c4", 
            golden="42f26aad0b5d05f93b3302abdc59c778788dc5c4",
            jest_test_files=["libtransmission/announcer-udp.cc", "libtransmission/handshake.cc", "libtransmission/net.cc", "libtransmission/peer-io.cc", "libtransmission/torrent.cc", "tests/libtransmission/announcer-udp-test.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/net-test.cc", "tests/libtransmission/settings-test.cc"], 
        )
    ])

@problem(
    id="transmission-250e055",
    description="""
    fix: warnings from clang tidy sonarcloud coverity (#4143)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="48e42ac71e8a9532016d2884bee8cf7568ddd88a",
    test="250e055c1d69295b6d73a7ce00fec404db3e9329", 
    golden="250e055c1d69295b6d73a7ce00fec404db3e9329",
)
def transmission_250e055(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="48e42ac71e8a9532016d2884bee8cf7568ddd88a",
            test="250e055c1d69295b6d73a7ce00fec404db3e9329", 
            golden="250e055c1d69295b6d73a7ce00fec404db3e9329",
            jest_test_files=["libtransmission/announcer-udp.cc", "libtransmission/blocklist.cc", "libtransmission/handshake.cc", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "libtransmission/peer-mgr.cc", "libtransmission/session-thread.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/utils-ev.h", "libtransmission/utils.cc", "qt/MakeDialog.cc", "tests/libtransmission/dht-test.cc", "tests/libtransmission/handshake-test.cc", "tests/libtransmission/watchdir-test.cc"], 
        )
    ])

@problem(
    id="transmission-2d2270c",
    description="""
    fix: thread-sanitizer warnings in SandboxedTests (#4131)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="7e817b5a43292d9d579dd6b1f5c196a73070cdc1",
    test="2d2270c7d9015a6eeac5a7d5cf2ec4335aa7bf69", 
    golden="2d2270c7d9015a6eeac5a7d5cf2ec4335aa7bf69",
)
def transmission_2d2270c(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="7e817b5a43292d9d579dd6b1f5c196a73070cdc1",
            test="2d2270c7d9015a6eeac5a7d5cf2ec4335aa7bf69", 
            golden="2d2270c7d9015a6eeac5a7d5cf2ec4335aa7bf69",
            jest_test_files=["tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-4ea9c87",
    description="""
    fix: some typos (#3904)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="20c2fde7aece077eefff689a3c3dc478e59a74a2",
    test="4ea9c87feac9ae62f48b2180b153926e1a16c89d", 
    golden="4ea9c87feac9ae62f48b2180b153926e1a16c89d",
)
def transmission_4ea9c87(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="20c2fde7aece077eefff689a3c3dc478e59a74a2",
            test="4ea9c87feac9ae62f48b2180b153926e1a16c89d", 
            golden="4ea9c87feac9ae62f48b2180b153926e1a16c89d",
            jest_test_files=["AUTHORS", "docs/Port-Forwarding-Guide.md", "docs/README.md", "docs/Release-Notes.md", "extras/encryption.txt", "gtk/ui/gtk3/PrefsDialog.ui", "gtk/ui/gtk4/PrefsDialog.ui", "libtransmission/handshake.cc", "libtransmission/jsonsl.c", "libtransmission/peer-mgr.cc", "libtransmission/transmission.h", "macosx/Controller.mm", "macosx/CreatorWindowController.mm", "macosx/Credits.rtf", "macosx/Torrent.mm", "macosx/TransmissionHelp/html/usingt.html", "news/news-2.42-and-older.md", "news/news-4.0.0-beta-1.md", "tests/libtransmission/handshake-test.cc", "web/src/formatter.js", "web/src/torrent.js"], 
        )
    ])

@problem(
    id="transmission-ecc7c18",
    description="""
    tests: Fix SubprocessTest on macOS Monterey and later. (#3812)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f8fdc6a8286e8429c8dfbb6b662864aa2d67ec0a",
    test="ecc7c185a4a7801b83bff35d9c5e848dc58f925a", 
    golden="ecc7c185a4a7801b83bff35d9c5e848dc58f925a",
)
def transmission_ecc7c18(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f8fdc6a8286e8429c8dfbb6b662864aa2d67ec0a",
            test="ecc7c185a4a7801b83bff35d9c5e848dc58f925a", 
            golden="ecc7c185a4a7801b83bff35d9c5e848dc58f925a",
            jest_test_files=["tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-89d6533",
    description="""
    build: support semver versioning (#3867)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="fff4c877407ff3d281c08938a6161cdcacfc0191",
    test="89d6533cd743519e566153326bca107a4514376b", 
    golden="89d6533cd743519e566153326bca107a4514376b",
)
def transmission_89d6533(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="fff4c877407ff3d281c08938a6161cdcacfc0191",
            test="89d6533cd743519e566153326bca107a4514376b", 
            golden="89d6533cd743519e566153326bca107a4514376b",
            jest_test_files=["CMakeLists.txt", "cmake/Transmission.rc.in", "dist/msi/CMakeLists.txt", "libtransmission/clients.cc", "libtransmission/version.h.in", "tests/libtransmission/clients-test.cc", "update-version-h.sh"], 
        )
    ])

@problem(
    id="transmission-76fc42b",
    description="""
    test: fix watchdir CI flake (#3839)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="228efa16e3299ede3f6419e628c6decb1f67baf3",
    test="76fc42b6599dc9daa2b2d8a24c66ec1ec57c1888", 
    golden="76fc42b6599dc9daa2b2d8a24c66ec1ec57c1888",
)
def transmission_76fc42b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="228efa16e3299ede3f6419e628c6decb1f67baf3",
            test="76fc42b6599dc9daa2b2d8a24c66ec1ec57c1888", 
            golden="76fc42b6599dc9daa2b2d8a24c66ec1ec57c1888",
            jest_test_files=["tests/libtransmission/watchdir-test.cc"], 
        )
    ])

@problem(
    id="transmission-9fb590d",
    description="""
    fix: recent coverity warnings (#3788)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b41501eeb8d473768120873f03134b81bf48cdb0",
    test="9fb590d3f5f65dcc991c0e689fe7131306f76ffb", 
    golden="9fb590d3f5f65dcc991c0e689fe7131306f76ffb",
)
def transmission_9fb590d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b41501eeb8d473768120873f03134b81bf48cdb0",
            test="9fb590d3f5f65dcc991c0e689fe7131306f76ffb", 
            golden="9fb590d3f5f65dcc991c0e689fe7131306f76ffb",
            jest_test_files=["libtransmission/peer-msgs.cc", "libtransmission/verify.cc", "tests/libtransmission/file-test.cc"], 
        )
    ])

@problem(
    id="transmission-dde626d",
    description="""
    refactor: remove unused (#3675)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c532728c428b51183f48befcc12c9a8af611979f",
    test="dde626d5e5b9ec4e66dc6ee45addb7e21a1de132", 
    golden="dde626d5e5b9ec4e66dc6ee45addb7e21a1de132",
)
def transmission_dde626d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c532728c428b51183f48befcc12c9a8af611979f",
            test="dde626d5e5b9ec4e66dc6ee45addb7e21a1de132", 
            golden="dde626d5e5b9ec4e66dc6ee45addb7e21a1de132",
            jest_test_files=["libtransmission/file-win32.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/tr-macros.h", "libtransmission/transmission.h", "tests/libtransmission/session-test.cc"], 
        )
    ])

@problem(
    id="transmission-988d8ff",
    description="""
    test: possibly fix rename-test flakes (#3653)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="6278ea7017e7cb6525cfe7165b169e15059dde7f",
    test="988d8ff9ace1018f2ba5fbedb7c5532ed392658a", 
    golden="988d8ff9ace1018f2ba5fbedb7c5532ed392658a",
)
def transmission_988d8ff(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="6278ea7017e7cb6525cfe7165b169e15059dde7f",
            test="988d8ff9ace1018f2ba5fbedb7c5532ed392658a", 
            golden="988d8ff9ace1018f2ba5fbedb7c5532ed392658a",
            jest_test_files=[".github/workflows/actions.yml", "tests/libtransmission/rename-test.cc", "tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-c7466b3",
    description="""
    fix: coverity warnings (#3632)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1c8032d23aca43e9366258d9bac03a4f4adae2bb",
    test="c7466b3ff4bb564a692cf137dcdbae98bc31a29e", 
    golden="c7466b3ff4bb564a692cf137dcdbae98bc31a29e",
)
def transmission_c7466b3(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1c8032d23aca43e9366258d9bac03a4f4adae2bb",
            test="c7466b3ff4bb564a692cf137dcdbae98bc31a29e", 
            golden="c7466b3ff4bb564a692cf137dcdbae98bc31a29e",
            jest_test_files=["gtk/Application.cc", "gtk/FaviconCache.cc", "libtransmission/.clang-tidy", "libtransmission/bandwidth.cc", "libtransmission/file-posix.cc", "libtransmission/handshake.cc", "libtransmission/makemeta.cc", "libtransmission/natpmp_local.h", "libtransmission/peer-mgr.cc", "libtransmission/port-forwarding.cc", "libtransmission/rpc-server.cc", "libtransmission/session-id.h", "libtransmission/session.h", "libtransmission/timer-ev.cc", "libtransmission/utils.cc", "tests/libtransmission/announce-list-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/watchdir-test.cc", "utils/create.cc"], 
        )
    ])

@problem(
    id="transmission-b1cc968",
    description="""
    Fix out-of-bounds read in torrent parsing (#3600)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="a5f7df34abb747cfe71c6d7196d2fcf6b0446e5c",
    test="b1cc968969907951dcc114a4622a4969476bb8b9", 
    golden="b1cc968969907951dcc114a4622a4969476bb8b9",
)
def transmission_b1cc968(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="a5f7df34abb747cfe71c6d7196d2fcf6b0446e5c",
            test="b1cc968969907951dcc114a4622a4969476bb8b9", 
            golden="b1cc968969907951dcc114a4622a4969476bb8b9",
            jest_test_files=["libtransmission/torrent-metainfo.cc", "tests/libtransmission/torrent-metainfo-test.cc"], 
        )
    ])

@problem(
    id="transmission-83ffa6b",
    description="""
    chore: fix spdx abbreviations (#3602)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="31a733fab769302202ea24053680a1372f334c22",
    test="83ffa6bf1b3408bc33f419890442da7898b45c02", 
    golden="83ffa6bf1b3408bc33f419890442da7898b45c02",
)
def transmission_83ffa6b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="31a733fab769302202ea24053680a1372f334c22",
            test="83ffa6bf1b3408bc33f419890442da7898b45c02", 
            golden="83ffa6bf1b3408bc33f419890442da7898b45c02",
            jest_test_files=["daemon/daemon.h", "gtk/Actions.h", "gtk/DetailsDialog.h", "gtk/FaviconCache.h", "gtk/FileList.h", "gtk/FilterBar.h", "gtk/FreeSpaceLabel.h", "gtk/HigWorkarea.h", "gtk/MakeDialog.h", "gtk/MessageLogWindow.h", "gtk/Notify.h", "gtk/OptionsDialog.h", "gtk/PrefsDialog.h", "gtk/RelocateDialog.h", "gtk/StatsDialog.h", "gtk/SystemTrayIcon.h", "gtk/TorrentCellRenderer.h", "gtk/Utils.h", "libtransmission/announce-list.h", "libtransmission/announcer-common.h", "libtransmission/announcer.h", "libtransmission/bandwidth.h", "libtransmission/benc.h", "libtransmission/bitfield.h", "libtransmission/block-info.h", "libtransmission/blocklist.h", "libtransmission/cache.h", "libtransmission/clients.h", "libtransmission/completion.h", "libtransmission/crypto-utils.h", "libtransmission/error-types.h", "libtransmission/error.h", "libtransmission/file-piece-map.h", "libtransmission/file.h", "libtransmission/handshake.h", "libtransmission/history.h", "libtransmission/inout.h", "libtransmission/interned-string.h", "libtransmission/log.h", "libtransmission/lru-cache.h", "libtransmission/magnet-metainfo.h", "libtransmission/makemeta.h", "libtransmission/mime-types.h", "libtransmission/mime-types.js", "libtransmission/natpmp_local.h", "libtransmission/open-files.h", "libtransmission/peer-common.h", "libtransmission/peer-io.h", "libtransmission/peer-mgr-active-requests.h", "libtransmission/peer-mgr-wishlist.h", "libtransmission/peer-mgr.h", "libtransmission/peer-mse.h", "libtransmission/peer-msgs.h", "libtransmission/peer-socket.h", "libtransmission/platform-quota.h", "libtransmission/platform.h", "libtransmission/port-forwarding.h", "libtransmission/quark.h", "libtransmission/resume.h", "libtransmission/rpc-server.h", "libtransmission/rpcimpl.h", "libtransmission/session-id.h", "libtransmission/session.h", "libtransmission/stats.cc", "libtransmission/stats.h", "libtransmission/subprocess.h", "libtransmission/torrent-files.cc", "libtransmission/torrent-files.h", "libtransmission/torrent-magnet.h", "libtransmission/torrent-metainfo.h", "libtransmission/torrent.h", "libtransmission/torrents.cc", "libtransmission/torrents.h", "libtransmission/tr-assert.h", "libtransmission/tr-assert.mm", "libtransmission/tr-getopt.h", "libtransmission/tr-macros.h", "libtransmission/tr-strbuf.h", "libtransmission/trevent.h", "libtransmission/upnp.h", "libtransmission/utils.h", "libtransmission/variant-common.h", "libtransmission/variant.h", "libtransmission/verify.h", "libtransmission/watchdir-common.h", "libtransmission/watchdir.h", "libtransmission/web-utils.h", "libtransmission/web.h", "libtransmission/webseed.h", "qt/AboutDialog.h", "qt/AddData.h", "qt/Application.h", "qt/BaseDialog.h", "qt/ColumnResizer.h", "qt/ComInteropHelper.h", "qt/CustomVariantType.h", "qt/DBusInteropHelper.h", "qt/DetailsDialog.h", "qt/FaviconCache.h", "qt/FileTreeDelegate.h", "qt/FileTreeItem.h", "qt/FileTreeModel.h", "qt/FileTreeView.h", "qt/FilterBar.h", "qt/FilterBarComboBox.h", "qt/FilterBarComboBoxDelegate.h", "qt/Filters.h", "qt/Formatter.h", "qt/FreeSpaceLabel.h", "qt/IconCache.h", "qt/IconToolButton.h", "qt/InteropHelper.h", "qt/InteropObject.h", "qt/LicenseDialog.h", "qt/MainWindow.h", "qt/MakeDialog.h", "qt/OptionsDialog.h", "qt/PathButton.h", "qt/Prefs.h", "qt/PrefsDialog.h", "qt/RelocateDialog.h", "qt/RpcClient.h", "qt/RpcQueue.h", "qt/Session.h", "qt/SessionDialog.h", "qt/Speed.h", "qt/StatsDialog.h", "qt/StyleHelper.h", "qt/Torrent.h", "qt/TorrentDelegate.h", "qt/TorrentDelegateMin.h", "qt/TorrentFilter.h", "qt/TorrentModel.h", "qt/TorrentView.h", "qt/TrackerDelegate.h", "qt/TrackerModel.h", "qt/TrackerModelFilter.h", "qt/Utils.h", "qt/VariantHelpers.h", "qt/WatchDir.h", "tests/libtransmission/announce-list-test.cc", "tests/libtransmission/announcer-test.cc", "tests/libtransmission/benc-test.cc", "tests/libtransmission/bitfield-test.cc", "tests/libtransmission/block-info-test.cc", "tests/libtransmission/blocklist-test.cc", "tests/libtransmission/clients-test.cc", "tests/libtransmission/completion-test.cc", "tests/libtransmission/copy-test.cc", "tests/libtransmission/crypto-test-ref.h", "tests/libtransmission/crypto-test.cc", "tests/libtransmission/error-test.cc", "tests/libtransmission/file-piece-map-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/getopt-test.cc", "tests/libtransmission/handshake-test.cc", "tests/libtransmission/history-test.cc", "tests/libtransmission/json-test.cc", "tests/libtransmission/magnet-metainfo-test.cc", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/move-test.cc", "tests/libtransmission/open-files-test.cc", "tests/libtransmission/peer-mgr-active-requests-test.cc", "tests/libtransmission/peer-mgr-wishlist-test.cc", "tests/libtransmission/peer-msgs-test.cc", "tests/libtransmission/platform-test.cc", "tests/libtransmission/quark-test.cc", "tests/libtransmission/remove-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/rpc-test.cc", "tests/libtransmission/session-test.cc", "tests/libtransmission/strbuf-test.cc", "tests/libtransmission/subprocess-test-program.cc", "tests/libtransmission/subprocess-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/torrent-files-test.cc", "tests/libtransmission/torrent-metainfo-test.cc", "tests/libtransmission/torrents-test.cc", "tests/libtransmission/utils-test.cc", "tests/libtransmission/variant-test.cc", "tests/libtransmission/watchdir-test.cc", "tests/libtransmission/web-utils-test.cc", "utils/show.cc", "utils/units.h"], 
        )
    ])

@problem(
    id="transmission-8b983b3",
    description="""
    refactor: tr_sys_path_resolve() returns a std::string (#3587)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="3ed6b187bb3e421263dcee843c0780cfa6be02f2",
    test="8b983b3d1ccb521ae485d51a3e186a4fd022998d", 
    golden="8b983b3d1ccb521ae485d51a3e186a4fd022998d",
)
def transmission_8b983b3(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="3ed6b187bb3e421263dcee843c0780cfa6be02f2",
            test="8b983b3d1ccb521ae485d51a3e186a4fd022998d", 
            golden="8b983b3d1ccb521ae485d51a3e186a4fd022998d",
            jest_test_files=["CMakeLists.txt", "libtransmission/file-posix.cc", "libtransmission/file-win32.cc", "libtransmission/file.h", "libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/variant-benc.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/subprocess-test.cc"], 
        )
    ])

@problem(
    id="transmission-ec79a2a",
    description="""
    fix: clang-tidy misc-const-correctness warnings (#3529)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="78b24b594ba629cbf0d1bd8187513ae06ac50b5b",
    test="ec79a2a888d1564df03b9b3ee08128ae042c2c20", 
    golden="ec79a2a888d1564df03b9b3ee08128ae042c2c20",
)
def transmission_ec79a2a(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="78b24b594ba629cbf0d1bd8187513ae06ac50b5b",
            test="ec79a2a888d1564df03b9b3ee08128ae042c2c20", 
            golden="ec79a2a888d1564df03b9b3ee08128ae042c2c20",
            jest_test_files=["libtransmission/announcer-http.cc", "libtransmission/announcer.cc", "libtransmission/bitfield.cc", "libtransmission/crypto-utils.cc", "libtransmission/file-posix.cc", "libtransmission/handshake.cc", "libtransmission/magnet-metainfo.cc", "libtransmission/peer-io.cc", "libtransmission/peer-mgr.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "libtransmission/torrent-magnet.cc", "libtransmission/tr-dht.cc", "libtransmission/tr-lpd.cc", "libtransmission/tr-udp.cc", "libtransmission/upnp.cc", "libtransmission/utils.cc", "qt/Application.cc", "qt/DetailsDialog.cc", "qt/FaviconCache.cc", "qt/FileTreeModel.cc", "qt/FileTreeView.cc", "qt/FilterBarComboBox.cc", "qt/IconCache.cc", "qt/MainWindow.cc", "qt/MakeDialog.cc", "qt/Prefs.cc", "qt/PrefsDialog.cc", "qt/RpcClient.cc", "qt/RpcQueue.cc", "qt/SqueezeLabel.cc", "qt/Torrent.cc", "qt/TorrentDelegate.cc", "qt/TorrentFilter.cc", "qt/TrackerDelegate.cc", "qt/TrackerModel.cc", "qt/TrackerModelFilter.cc", "tests/libtransmission/bitfield-test.cc", "tests/libtransmission/copy-test.cc", "tests/libtransmission/file-piece-map-test.cc", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-445aad5",
    description="""
    test: add platform tests (#3514)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="9bf2918ad09ee6c89e105adfb865d9130f987bed",
    test="445aad56a0054b7b1e5c0fc995e161db6531f1ff", 
    golden="445aad56a0054b7b1e5c0fc995e161db6531f1ff",
)
def transmission_445aad5(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="9bf2918ad09ee6c89e105adfb865d9130f987bed",
            test="445aad56a0054b7b1e5c0fc995e161db6531f1ff", 
            golden="445aad56a0054b7b1e5c0fc995e161db6531f1ff",
            jest_test_files=["cli/cli.cc", "gtk/Prefs.cc", "gtk/main.cc", "libtransmission/platform.cc", "libtransmission/platform.h", "libtransmission/rpc-server.cc", "libtransmission/rpc-server.h", "libtransmission/session.cc", "libtransmission/transmission.h", "macosx/Controller.mm", "qt/Application.cc", "qt/Prefs.cc", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/assets/user-dirs.dirs", "tests/libtransmission/platform-test.cc"], 
        )
    ])

@problem(
    id="transmission-0da1cbb",
    description="""
    fix: 3508 location invalidation (#3511)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c50da43ae0751b09d80a40dfba7a3676c000f8d9",
    test="0da1cbb6ecaa405ec36a3736924cd20f4822ed2a", 
    golden="0da1cbb6ecaa405ec36a3736924cd20f4822ed2a",
)
def transmission_0da1cbb(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c50da43ae0751b09d80a40dfba7a3676c000f8d9",
            test="0da1cbb6ecaa405ec36a3736924cd20f4822ed2a", 
            golden="0da1cbb6ecaa405ec36a3736924cd20f4822ed2a",
            jest_test_files=["daemon/daemon.cc", "gtk/Application.cc", "gtk/Session.cc", "gtk/Session.h", "libtransmission/platform.cc", "libtransmission/platform.h", "libtransmission/resume.cc", "libtransmission/rpc-server.cc", "libtransmission/rpc-server.h", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/stats.cc", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/tr-dht.cc", "libtransmission/transmission.h", "tests/libtransmission/blocklist-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/move-test.cc"], 
        )
    ])

@problem(
    id="transmission-c50da43",
    description="""
    refactor: remove tr_sessionGetConfigDir() (#3506)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="3f5b439fccab39a9929b0d497631ce89499cdfa1",
    test="c50da43ae0751b09d80a40dfba7a3676c000f8d9", 
    golden="c50da43ae0751b09d80a40dfba7a3676c000f8d9",
)
def transmission_c50da43(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="3f5b439fccab39a9929b0d497631ce89499cdfa1",
            test="c50da43ae0751b09d80a40dfba7a3676c000f8d9", 
            golden="c50da43ae0751b09d80a40dfba7a3676c000f8d9",
            jest_test_files=["daemon/daemon.cc", "gtk/Application.cc", "gtk/Session.cc", "gtk/Session.h", "libtransmission/platform.cc", "libtransmission/platform.h", "libtransmission/resume.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/stats.cc", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/tr-dht.cc", "libtransmission/transmission.h", "tests/libtransmission/blocklist-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/move-test.cc"], 
        )
    ])

@problem(
    id="transmission-f8b3514",
    description="""
    tr_makeMetaInfo: new anonymize option (closes #3420) (#3452)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="94eeebc5b309f38b648a179612bcee4e1c05c73f",
    test="f8b3514c0e13329be8d6104f3764d01288a69246", 
    golden="f8b3514c0e13329be8d6104f3764d01288a69246",
)
def transmission_f8b3514(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="94eeebc5b309f38b648a179612bcee4e1c05c73f",
            test="f8b3514c0e13329be8d6104f3764d01288a69246", 
            golden="f8b3514c0e13329be8d6104f3764d01288a69246",
            jest_test_files=["gtk/MakeDialog.cc", "libtransmission/makemeta.cc", "libtransmission/makemeta.h", "macosx/CreatorWindowController.mm", "qt/MakeDialog.cc", "tests/libtransmission/makemeta-test.cc", "utils/create.cc", "utils/transmission-create.1"], 
        )
    ])

@problem(
    id="transmission-41c0f88",
    description="""
    fix: limit pad search during encrypted handshake (#3471)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="fb431cb1c16ba5974ebd58b7cd6a7c263e7b90f7",
    test="41c0f8885e1fd086c27afd2ae46a0c5c04ea1e74", 
    golden="41c0f8885e1fd086c27afd2ae46a0c5c04ea1e74",
)
def transmission_41c0f88(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="fb431cb1c16ba5974ebd58b7cd6a7c263e7b90f7",
            test="41c0f8885e1fd086c27afd2ae46a0c5c04ea1e74", 
            golden="41c0f8885e1fd086c27afd2ae46a0c5c04ea1e74",
            jest_test_files=["libtransmission/handshake.cc", "tests/libtransmission/handshake-test.cc"], 
        )
    ])

@problem(
    id="transmission-c3db52e",
    description="""
    Fix #3444, support single file hybrid torrents. (#3446)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="39d442b3ee6af17d05bb544a1368ecdff910d0bd",
    test="c3db52e31015c67f79f08a3fda81c26a84c40983", 
    golden="c3db52e31015c67f79f08a3fda81c26a84c40983",
)
def transmission_c3db52e(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="39d442b3ee6af17d05bb544a1368ecdff910d0bd",
            test="c3db52e31015c67f79f08a3fda81c26a84c40983", 
            golden="c3db52e31015c67f79f08a3fda81c26a84c40983",
            jest_test_files=["libtransmission/torrent-metainfo.cc", "tests/utils/CMakeLists.txt", "tests/utils/assets/hybrid-single-ubuntu-20.04.3-desktop-amd64.iso.show", "tests/utils/assets/hybrid-single-ubuntu-20.04.3-desktop-amd64.iso.torrent"], 
        )
    ])

@problem(
    id="transmission-e9a7ddf",
    description="""
    fix: minor warnings (#3413)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="9dfb3bf3df6bc06032eff9a84a63d5a8890892a9",
    test="e9a7ddf7f941046715e19b29a167efe17170e12e", 
    golden="e9a7ddf7f941046715e19b29a167efe17170e12e",
)
def transmission_e9a7ddf(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="9dfb3bf3df6bc06032eff9a84a63d5a8890892a9",
            test="e9a7ddf7f941046715e19b29a167efe17170e12e", 
            golden="e9a7ddf7f941046715e19b29a167efe17170e12e",
            jest_test_files=["libtransmission/torrent-magnet.cc", "tests/libtransmission/blocklist-test.cc", "tests/libtransmission/torrent-metainfo-test.cc"], 
        )
    ])

@problem(
    id="transmission-513f4bc",
    description="""
    fix: assertion failed 's->leftUntilDone <= s->sizeWhenDone' (#3406)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="707fce44da8ede86761c4b5611722bbd5bc7982e",
    test="513f4bc91b579e4a8f25edf68242dccba1500850", 
    golden="513f4bc91b579e4a8f25edf68242dccba1500850",
)
def transmission_513f4bc(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="707fce44da8ede86761c4b5611722bbd5bc7982e",
            test="513f4bc91b579e4a8f25edf68242dccba1500850", 
            golden="513f4bc91b579e4a8f25edf68242dccba1500850",
            jest_test_files=["libtransmission/block-info.h", "libtransmission/completion.cc", "libtransmission/completion.h", "tests/libtransmission/completion-test.cc"], 
        )
    ])

@problem(
    id="transmission-142b2a0",
    description="""
    Support wolfSSL 4.6+ (#3398)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="083529c5bb43afaad7d53df295407ff4d8a7a20c",
    test="142b2a088d64c85a0304dd4decdcb75cb93efeec", 
    golden="142b2a088d64c85a0304dd4decdcb75cb93efeec",
)
def transmission_142b2a0(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="083529c5bb43afaad7d53df295407ff4d8a7a20c",
            test="142b2a088d64c85a0304dd4decdcb75cb93efeec", 
            golden="142b2a088d64c85a0304dd4decdcb75cb93efeec",
            jest_test_files=["libtransmission/crypto-utils-cyassl.cc", "libtransmission/crypto.cc", "tests/libtransmission/CMakeLists.txt"], 
        )
    ])

@problem(
    id="transmission-3237323",
    description="""
    Add basic support for v2 hashes in transmission-show (#3380)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="85a7d0e09d98e57a878670dd7ad28e8a18cad7e3",
    test="3237323b8e665f400acefdd6f7185a09d574e8a9", 
    golden="3237323b8e665f400acefdd6f7185a09d574e8a9",
)
def transmission_3237323(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="85a7d0e09d98e57a878670dd7ad28e8a18cad7e3",
            test="3237323b8e665f400acefdd6f7185a09d574e8a9", 
            golden="3237323b8e665f400acefdd6f7185a09d574e8a9",
            jest_test_files=["CMakeLists.txt", "libtransmission/crypto-utils-ccrypto.cc", "libtransmission/crypto-utils-cyassl.cc", "libtransmission/crypto-utils-openssl.cc", "libtransmission/crypto-utils-polarssl.cc", "libtransmission/crypto-utils.cc", "libtransmission/crypto-utils.h", "libtransmission/magnet-metainfo.cc", "libtransmission/magnet-metainfo.h", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent-metainfo.h", "libtransmission/tr-macros.h", "tests/libtransmission/crypto-test-ref.h", "tests/libtransmission/crypto-test.cc", "tests/utils/CMakeLists.txt", "tests/utils/assets/Inner_Sanctum_movie_archive.show", "tests/utils/assets/Thor_and_the_Amazon_Women.avi.show", "tests/utils/assets/bittorrent-v2-hybrid-test.show", "tests/utils/assets/bittorrent-v2-hybrid-test.torrent", "tests/utils/assets/bittorrent-v2-test.show", "tests/utils/assets/ubuntu-20.04.3-desktop-amd64.iso.show", "utils/show.cc"], 
        )
    ])

@problem(
    id="transmission-85c11b7",
    description="""
    fix: requests across piece boundaries when piece is not a multiple of block_size
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b983a3ba5c878a1683ccd602c5647c56aade8b6a",
    test="85c11b7f03016a4c242fc5e14a6ca1c3be8e3702", 
    golden="85c11b7f03016a4c242fc5e14a6ca1c3be8e3702",
)
def transmission_85c11b7(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b983a3ba5c878a1683ccd602c5647c56aade8b6a",
            test="85c11b7f03016a4c242fc5e14a6ca1c3be8e3702", 
            golden="85c11b7f03016a4c242fc5e14a6ca1c3be8e3702",
            jest_test_files=["libtransmission/cache.cc", "libtransmission/cache.h", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "libtransmission/peer-mgr-wishlist.cc", "libtransmission/peer-msgs.cc", "libtransmission/torrent.h", "libtransmission/webseed.cc", "tests/libtransmission/move-test.cc"], 
        )
    ])

@problem(
    id="transmission-34cb56b",
    description="""
    refactor: remove unused tr_ptrArray class (#3262)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d34bd0b4d6417da24b7decb192bf75a33881c9e3",
    test="34cb56b2af75afb11697850e2e2dd7f27e842d0c", 
    golden="34cb56b2af75afb11697850e2e2dd7f27e842d0c",
)
def transmission_34cb56b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d34bd0b4d6417da24b7decb192bf75a33881c9e3",
            test="34cb56b2af75afb11697850e2e2dd7f27e842d0c", 
            golden="34cb56b2af75afb11697850e2e2dd7f27e842d0c",
            jest_test_files=[".github/workflows/sanitizer-clang.yml", ".github/workflows/sanitizer-gcc.yml", "Transmission.xcodeproj/project.pbxproj", "libtransmission/CMakeLists.txt", "libtransmission/ptrarray.cc", "libtransmission/ptrarray.h", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-256b436",
    description="""
    fix: clang 15 warnings (#3172)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="26ed2a0ec823762d61494326baaeeaf7a1d1970b",
    test="256b4360232c792bd6a1fa556c23e2fdbee41eb4", 
    golden="256b4360232c792bd6a1fa556c23e2fdbee41eb4",
)
def transmission_256b436(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="26ed2a0ec823762d61494326baaeeaf7a1d1970b",
            test="256b4360232c792bd6a1fa556c23e2fdbee41eb4", 
            golden="256b4360232c792bd6a1fa556c23e2fdbee41eb4",
            jest_test_files=["libtransmission/announcer.cc", "libtransmission/clients.cc", "libtransmission/completion.cc", "libtransmission/crypto-utils.cc", "libtransmission/crypto.cc", "libtransmission/handshake.cc", "libtransmission/inout.cc", "libtransmission/peer-io.cc", "libtransmission/peer-mgr.cc", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent.cc", "libtransmission/tr-macros.h", "libtransmission/tr-udp.cc", "qt/.clang-tidy", "tests/libtransmission/.clang-tidy"], 
        )
    ])

@problem(
    id="transmission-84d65d8",
    description="""
    fix: coverity warnings (#3168)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1c3d60fcd5c75f96dbb7f7e9bb3b0fa3569fedc3",
    test="84d65d8e6184351dcf36e7491eb04efbe982edb0", 
    golden="84d65d8e6184351dcf36e7491eb04efbe982edb0",
)
def transmission_84d65d8(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1c3d60fcd5c75f96dbb7f7e9bb3b0fa3569fedc3",
            test="84d65d8e6184351dcf36e7491eb04efbe982edb0", 
            golden="84d65d8e6184351dcf36e7491eb04efbe982edb0",
            jest_test_files=["gtk/FaviconCache.cc", "libtransmission/handshake.cc", "libtransmission/peer-mgr.cc", "tests/libtransmission/open-files-test.cc"], 
        )
    ])

@problem(
    id="transmission-67a0784",
    description="""
    fix: compiler warnings (#3123)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="c0bb2d40f123f99dca5d152087317706c09edaa8",
    test="67a078402d570021006a2996fa8b7964bf008cb8", 
    golden="67a078402d570021006a2996fa8b7964bf008cb8",
)
def transmission_67a0784(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="c0bb2d40f123f99dca5d152087317706c09edaa8",
            test="67a078402d570021006a2996fa8b7964bf008cb8", 
            golden="67a078402d570021006a2996fa8b7964bf008cb8",
            jest_test_files=["libtransmission/bitfield.cc", "libtransmission/blocklist.cc", "libtransmission/blocklist.h", "libtransmission/rpc-server.cc", "qt/DetailsDialog.cc", "qt/MainWindow.cc", "tests/libtransmission/blocklist-test.cc"], 
        )
    ])

@problem(
    id="transmission-c0bb2d4",
    description="""
    refactor: add pathbuf and std::string-friendly helpers to tr_sys file and path funcs (#3118)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="690cf50e539c20c77daf9d7db390d6306a3da157",
    test="c0bb2d40f123f99dca5d152087317706c09edaa8", 
    golden="c0bb2d40f123f99dca5d152087317706c09edaa8",
)
def transmission_c0bb2d4(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="690cf50e539c20c77daf9d7db390d6306a3da157",
            test="c0bb2d40f123f99dca5d152087317706c09edaa8", 
            golden="c0bb2d40f123f99dca5d152087317706c09edaa8",
            jest_test_files=["cli/cli.cc", "daemon/daemon.cc", "gtk/OptionsDialog.cc", "libtransmission/file.h", "libtransmission/makemeta.cc", "libtransmission/open-files.cc", "libtransmission/platform.cc", "libtransmission/session-id.cc", "libtransmission/torrent-metainfo.cc", "libtransmission/torrent.cc", "libtransmission/tr-strbuf.h", "libtransmission/utils.cc", "tests/libtransmission/blocklist-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/remove-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/torrent-metainfo-test.cc", "tests/libtransmission/utils-test.cc", "tests/libtransmission/watchdir-test.cc"], 
        )
    ])

@problem(
    id="transmission-a28b07b",
    description="""
    Revert 'refactor: move tr_torrent callbacks to tr_session (#3003)' (#3104)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="e23a4b35891d96dcf9614ddaa9595aea4a1b5563",
    test="a28b07b3904b98d0115a0fc929d690ba10054d60", 
    golden="a28b07b3904b98d0115a0fc929d690ba10054d60",
)
def transmission_a28b07b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="e23a4b35891d96dcf9614ddaa9595aea4a1b5563",
            test="a28b07b3904b98d0115a0fc929d690ba10054d60", 
            golden="a28b07b3904b98d0115a0fc929d690ba10054d60",
            jest_test_files=["gtk/Session.cc", "libtransmission/peer-mgr.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/transmission.h", "macosx/Torrent.mm", "tests/libtransmission/move-test.cc"], 
        )
    ])

@problem(
    id="transmission-bdac708",
    description="""
    docs: fix various typos and misspellings (#2955)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="0eb1857c6ce3250b6d906668cd785382f69c5f7c",
    test="bdac708762993d16a45dcdf966f906f00351cc60", 
    golden="bdac708762993d16a45dcdf966f906f00351cc60",
)
def transmission_bdac708(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="0eb1857c6ce3250b6d906668cd785382f69c5f7c",
            test="bdac708762993d16a45dcdf966f906f00351cc60", 
            golden="bdac708762993d16a45dcdf966f906f00351cc60",
            jest_test_files=["CONTRIBUTING.md", "NEWS.md", "daemon/daemon-posix.cc", "docs/Port-Forwarding-Guide.md", "docs/Release-Notes.md", "extras/encryption.txt", "extras/extended-messaging.txt", "gtk/Application.cc", "libtransmission/announcer.cc", "libtransmission/announcer.h", "libtransmission/bitfield.cc", "libtransmission/bitfield.h", "libtransmission/blocklist.cc", "libtransmission/crypto-utils-ccrypto.cc", "libtransmission/handshake.cc", "libtransmission/jsonsl.c", "libtransmission/jsonsl.h", "libtransmission/libt.dox", "libtransmission/peer-io.cc", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/resume.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/rpcimpl.h", "libtransmission/session.cc", "libtransmission/torrent-files.cc", "libtransmission/torrent-metainfo.cc", "libtransmission/tr-dht.cc", "libtransmission/tr-lpd.cc", "libtransmission/tr-strbuf.h", "libtransmission/transmission.h", "libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/web.h", "macosx/BlocklistDownloader.h", "macosx/Controller.h", "macosx/Controller.mm", "macosx/FileNameCell.mm", "macosx/InfoTrackersViewController.mm", "macosx/NSStringAdditions.mm", "macosx/PiecesView.mm", "macosx/PrefsController.mm", "macosx/TrackerCell.mm", "macosx/TransmissionHelp/html/gettingstarted.html", "macosx/TransmissionHelp/html/network.html", "macosx/TransmissionHelp/html/peers.html", "po/fr_CA.po", "qt/MainWindow.h", "qt/PrefsDialog.ui", "tests/libtransmission/crypto-test.cc", "tests/libtransmission/peer-mgr-active-requests-test.cc", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-c1faebc",
    description="""
    fix: new MSVC warning in file-piece-map-test.cc (#2936)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="3ec7e1933e6779e6039aca6d3aa201216b72a9e5",
    test="c1faebca6ea0dd3a4c5c18660dae88d70a990d9c", 
    golden="c1faebca6ea0dd3a4c5c18660dae88d70a990d9c",
)
def transmission_c1faebc(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="3ec7e1933e6779e6039aca6d3aa201216b72a9e5",
            test="c1faebca6ea0dd3a4c5c18660dae88d70a990d9c", 
            golden="c1faebca6ea0dd3a4c5c18660dae88d70a990d9c",
            jest_test_files=["tests/libtransmission/file-piece-map-test.cc"], 
        )
    ])

@problem(
    id="transmission-f79a75c",
    description="""
    test: fuzz test tr_variantFromBuf() (#2892)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="a134445caa34904b491f8fdb5750223e237481e0",
    test="f79a75cb2114150b1fd9d7c80bdc02c5a512c808", 
    golden="f79a75cb2114150b1fd9d7c80bdc02c5a512c808",
)
def transmission_f79a75c(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="a134445caa34904b491f8fdb5750223e237481e0",
            test="f79a75cb2114150b1fd9d7c80bdc02c5a512c808", 
            golden="f79a75cb2114150b1fd9d7c80bdc02c5a512c808",
            jest_test_files=["libtransmission/benc.h", "libtransmission/variant-benc.cc", "libtransmission/variant-common.h", "libtransmission/variant-json.cc", "libtransmission/variant.cc", "tests/libtransmission/variant-test.cc"], 
        )
    ])

@problem(
    id="transmission-a134445",
    description="""
    test: fuzz test tr_torrent_metainfo.parseBenc() (#2891)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="e88ebbc3e5d566ca2d5f226ec208e23c99d7d601",
    test="a134445caa34904b491f8fdb5750223e237481e0", 
    golden="a134445caa34904b491f8fdb5750223e237481e0",
)
def transmission_a134445(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="e88ebbc3e5d566ca2d5f226ec208e23c99d7d601",
            test="a134445caa34904b491f8fdb5750223e237481e0", 
            golden="a134445caa34904b491f8fdb5750223e237481e0",
            jest_test_files=["libtransmission/variant-benc.cc", "tests/libtransmission/torrent-metainfo-test.cc", "tests/libtransmission/web-utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-eb33b2f",
    description="""
    fix: tr_clientForId() (#2887)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="7ff13825038cb1af3dc59e224190942f57d0de6b",
    test="eb33b2faf5f99809dc5e68f5782032bdea48b3f2", 
    golden="eb33b2faf5f99809dc5e68f5782032bdea48b3f2",
)
def transmission_eb33b2f(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="7ff13825038cb1af3dc59e224190942f57d0de6b",
            test="eb33b2faf5f99809dc5e68f5782032bdea48b3f2", 
            golden="eb33b2faf5f99809dc5e68f5782032bdea48b3f2",
            jest_test_files=["libtransmission/clients.cc", "tests/libtransmission/clients-test.cc"], 
        )
    ])

@problem(
    id="transmission-7aeb5d8",
    description="""
    Merge branch 'main' into nevack/mojave-infowindow-fix
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="7cf920a020cb031f27d086e4bff09f682a3aef4f",
    test="7aeb5d8b2fd54e8a3c7ad26812ba85a0acf8a301", 
    golden="7aeb5d8b2fd54e8a3c7ad26812ba85a0acf8a301",
)
def transmission_7aeb5d8(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="7cf920a020cb031f27d086e4bff09f682a3aef4f",
            test="7aeb5d8b2fd54e8a3c7ad26812ba85a0acf8a301", 
            golden="7aeb5d8b2fd54e8a3c7ad26812ba85a0acf8a301",
            jest_test_files=["README.md", "cli/cli.cc", "daemon/daemon.cc", "gtk/Application.cc", "gtk/DetailsDialog.cc", "gtk/FileList.cc", "gtk/IconCache.cc", "gtk/OptionsDialog.cc", "gtk/PrefsDialog.cc", "gtk/Utils.cc", "libtransmission/announcer.cc", "libtransmission/makemeta.cc", "libtransmission/net.cc", "libtransmission/peer-mgr-active-requests.cc", "libtransmission/peer-mgr.cc", "libtransmission/rpcimpl.cc", "libtransmission/tr-dht.cc", "libtransmission/tr-strbuf.h", "libtransmission/upnp.cc", "libtransmission/utils.cc", "libtransmission/utils.h", "libtransmission/variant-benc.cc", "libtransmission/variant-json.cc", "macosx/CMakeLists.txt", "macosx/Images/Images.xcassets/BlueDotFlat.imageset/BlueDotFlat.png", "macosx/Images/Images.xcassets/BlueDotFlat.imageset/BlueDotFlat@2x.png", "macosx/Images/Images.xcassets/BlueDotFlat.imageset/Contents.json", "macosx/Images/Images.xcassets/GreenDotFlat.imageset/Contents.json", "macosx/Images/Images.xcassets/GreenDotFlat.imageset/GreenDotFlat.png", "macosx/Images/Images.xcassets/GreenDotFlat.imageset/GreenDotFlat@2x.png", "macosx/Images/Images.xcassets/OrangeDotFlat.imageset/Contents.json", "macosx/Images/Images.xcassets/OrangeDotFlat.imageset/OrangeDotFlat.png", "macosx/Images/Images.xcassets/OrangeDotFlat.imageset/OrangeDotFlat@2x.png", "macosx/Images/Images.xcassets/PurpleDotFlat.imageset/PurpleDotFlat.png", "macosx/Images/Images.xcassets/PurpleDotFlat.imageset/PurpleDotFlat@2x.png", "macosx/Images/Images.xcassets/RedDotFlat.imageset/RedDotFlat.png", "macosx/Images/Images.xcassets/RedDotFlat.imageset/RedDotFlat@2x.png", "macosx/Images/Images.xcassets/YellowDotFlat.imageset/YellowDotFlat.png", "macosx/Images/Images.xcassets/YellowDotFlat.imageset/YellowDotFlat@2x.png", "macosx/MessageWindow.xib", "macosx/MessageWindowController.mm", "qt/DetailsDialog.cc", "qt/FilterBar.cc", "qt/FilterBarComboBox.cc", "qt/FilterBarComboBoxDelegate.cc", "qt/MainWindow.cc", "qt/TorrentModel.cc", "tests/libtransmission/copy-test.cc", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/move-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/utils-test.cc", "tests/libtransmission/web-utils-test.cc", "third-party/googletest", "utils/edit.cc", "utils/remote.cc"], 
        )
    ])

@problem(
    id="transmission-76f44b4",
    description="""
    fix: sonarcloud (#2868)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="748d3c22237730c0411381f383e3f590da27ff18",
    test="76f44b4b6fbf70dd7956e6b0eed063bba8f437bc", 
    golden="76f44b4b6fbf70dd7956e6b0eed063bba8f437bc",
)
def transmission_76f44b4(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="748d3c22237730c0411381f383e3f590da27ff18",
            test="76f44b4b6fbf70dd7956e6b0eed063bba8f437bc", 
            golden="76f44b4b6fbf70dd7956e6b0eed063bba8f437bc",
            jest_test_files=["gtk/Application.cc", "gtk/DetailsDialog.cc", "gtk/FileList.cc", "gtk/IconCache.cc", "gtk/OptionsDialog.cc", "gtk/PrefsDialog.cc", "gtk/Utils.cc", "libtransmission/announcer.cc", "libtransmission/peer-mgr-active-requests.cc", "libtransmission/peer-mgr.cc", "libtransmission/rpcimpl.cc", "libtransmission/utils.cc", "libtransmission/variant-json.cc", "qt/DetailsDialog.cc", "qt/FilterBar.cc", "qt/FilterBarComboBox.cc", "qt/FilterBarComboBoxDelegate.cc", "qt/MainWindow.cc", "qt/TorrentModel.cc", "tests/libtransmission/copy-test.cc", "tests/libtransmission/makemeta-test.cc", "tests/libtransmission/move-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/utils-test.cc", "tests/libtransmission/web-utils-test.cc", "utils/edit.cc", "utils/remote.cc"], 
        )
    ])

@problem(
    id="transmission-1cc9da2",
    description="""
    fix: sonarcloud (#2865)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="46cc95f72e71cebca660781d8f498287b4cb2bfd",
    test="1cc9da26ba4c40c8f8d228b70c5d4c9c6b61eb77", 
    golden="1cc9da26ba4c40c8f8d228b70c5d4c9c6b61eb77",
)
def transmission_1cc9da2(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="46cc95f72e71cebca660781d8f498287b4cb2bfd",
            test="1cc9da26ba4c40c8f8d228b70c5d4c9c6b61eb77", 
            golden="1cc9da26ba4c40c8f8d228b70c5d4c9c6b61eb77",
            jest_test_files=["gtk/Application.cc", "gtk/FaviconCache.cc", "libtransmission/announcer-udp.cc", "libtransmission/blocklist.cc", "libtransmission/handshake.cc", "libtransmission/log.cc", "libtransmission/magnet-metainfo.h", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "libtransmission/peer-msgs.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/trevent.h", "qt/FileTreeItem.cc", "qt/FileTreeItem.h", "qt/InteropHelper.cc", "qt/Prefs.cc", "qt/Torrent.cc", "tests/libtransmission/announce-list-test.cc", "tests/libtransmission/announcer-test.cc", "tests/libtransmission/assets/alice_in_wonderland_librivox_archive.torrent", "tests/libtransmission/assets/debian-11.2.0-amd64-DVD-1.iso.torrent.added", "tests/libtransmission/bitfield-test.cc", "tests/libtransmission/block-info-test.cc", "tests/libtransmission/completion-test.cc", "tests/libtransmission/file-piece-map-test.cc", "tests/libtransmission/history-test.cc", "tests/libtransmission/json-test.cc", "tests/libtransmission/magnet-metainfo-test.cc", "tests/libtransmission/peer-mgr-active-requests-test.cc", "tests/libtransmission/peer-mgr-wishlist-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/rpc-test.cc", "tests/libtransmission/session-test.cc", "tests/libtransmission/strbuf-test.cc", "tests/libtransmission/test-fixtures.h", "tests/libtransmission/torrent-metainfo-test.cc", "tests/libtransmission/utils-test.cc", "utils/remote.cc", "utils/show.cc"], 
        )
    ])

@problem(
    id="transmission-a250690",
    description="""
    fix: sonarcloud (#2860)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="6da591fe5780ad1456bcca363cdfedd093193895",
    test="a250690f30b36a509b969d8785708380f7dbda3f", 
    golden="a250690f30b36a509b969d8785708380f7dbda3f",
)
def transmission_a250690(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="6da591fe5780ad1456bcca363cdfedd093193895",
            test="a250690f30b36a509b969d8785708380f7dbda3f", 
            golden="a250690f30b36a509b969d8785708380f7dbda3f",
            jest_test_files=["cli/cli.cc", "gtk/Application.cc", "gtk/DetailsDialog.cc", "gtk/FreeSpaceLabel.cc", "gtk/FreeSpaceLabel.h", "gtk/IconCache.cc", "gtk/MainWindow.cc", "gtk/Prefs.cc", "gtk/Prefs.h", "gtk/PrefsDialog.cc", "gtk/Session.cc", "gtk/Utils.cc", "qt/DetailsDialog.cc", "qt/FileTreeModel.cc", "qt/TorrentModel.cc", "tests/libtransmission/crypto-test.cc", "tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-6e91136",
    description="""
    fix: three asan issues (#2851)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d943f069f5f40155e6adb3f9577114f38e2759ce",
    test="6e91136b53ff8acd6055e85bc0341e350f6b7111", 
    golden="6e91136b53ff8acd6055e85bc0341e350f6b7111",
)
def transmission_6e91136(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d943f069f5f40155e6adb3f9577114f38e2759ce",
            test="6e91136b53ff8acd6055e85bc0341e350f6b7111", 
            golden="6e91136b53ff8acd6055e85bc0341e350f6b7111",
            jest_test_files=["libtransmission/magnet-metainfo.cc", "tests/libtransmission/completion-test.cc", "tests/libtransmission/torrents-test.cc"], 
        )
    ])

@problem(
    id="transmission-4dd25d8",
    description="""
    fix: tr_strbuf move op loses zero-termination (#2843)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="66638cc80cc1f45c5c3614b46f97d048bb30393e",
    test="4dd25d81121235f6088ae96904a57cabea9ca116", 
    golden="4dd25d81121235f6088ae96904a57cabea9ca116",
)
def transmission_4dd25d8(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="66638cc80cc1f45c5c3614b46f97d048bb30393e",
            test="4dd25d81121235f6088ae96904a57cabea9ca116", 
            golden="4dd25d81121235f6088ae96904a57cabea9ca116",
            jest_test_files=["libtransmission/tr-strbuf.h", "tests/libtransmission/strbuf-test.cc"], 
        )
    ])

@problem(
    id="transmission-66638cc",
    description="""
    test: fix race condition in move-test (#2841)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="3dadeae700811372b4e9d1d298841111e1f33339",
    test="66638cc80cc1f45c5c3614b46f97d048bb30393e", 
    golden="66638cc80cc1f45c5c3614b46f97d048bb30393e",
)
def transmission_66638cc(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="3dadeae700811372b4e9d1d298841111e1f33339",
            test="66638cc80cc1f45c5c3614b46f97d048bb30393e", 
            golden="66638cc80cc1f45c5c3614b46f97d048bb30393e",
            jest_test_files=["libtransmission/torrent-metainfo.h", "tests/libtransmission/move-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/rpc-test.cc", "tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-bd895b5",
    description="""
    test: fix file-info test edge case (#2811)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="6e8f9f3ff08d1878ec272339384c8c6a8e0449b1",
    test="bd895b50526665c4c379a5670105cafe017d2ad1", 
    golden="bd895b50526665c4c379a5670105cafe017d2ad1",
)
def transmission_bd895b5(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="6e8f9f3ff08d1878ec272339384c8c6a8e0449b1",
            test="bd895b50526665c4c379a5670105cafe017d2ad1", 
            golden="bd895b50526665c4c379a5670105cafe017d2ad1",
            jest_test_files=["tests/libtransmission/file-test.cc"], 
        )
    ])

@problem(
    id="transmission-9c3acc7",
    description="""
    fixup: handle unhandled scrape/announce responses (#2701)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="798022ac77b5f5efa2e6d70393a8f1a936e598f8",
    test="9c3acc7e8aa2d67e16790871ae00413e7932d1b3", 
    golden="9c3acc7e8aa2d67e16790871ae00413e7932d1b3",
)
def transmission_9c3acc7(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="798022ac77b5f5efa2e6d70393a8f1a936e598f8",
            test="9c3acc7e8aa2d67e16790871ae00413e7932d1b3", 
            golden="9c3acc7e8aa2d67e16790871ae00413e7932d1b3",
            jest_test_files=["libtransmission/announcer-common.h", "libtransmission/announcer-http.cc", "libtransmission/announcer.cc", "libtransmission/net.cc", "libtransmission/net.h", "libtransmission/session.h", "tests/libtransmission/announcer-test.cc"], 
        )
    ])

@problem(
    id="transmission-13ad2b5",
    description="""
    refactor: always use a blocksize of 16 KB (#2694)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f7d74095ed8e9d209489cc5bc87a982e80fb3614",
    test="13ad2b58dcb4b4c3e1af446dfe28c843e02b1827", 
    golden="13ad2b58dcb4b4c3e1af446dfe28c843e02b1827",
)
def transmission_13ad2b5(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f7d74095ed8e9d209489cc5bc87a982e80fb3614",
            test="13ad2b58dcb4b4c3e1af446dfe28c843e02b1827", 
            golden="13ad2b58dcb4b4c3e1af446dfe28c843e02b1827",
            jest_test_files=["libtransmission/block-info.cc", "libtransmission/block-info.h", "libtransmission/completion.cc", "libtransmission/inout.cc", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/torrent-metainfo.h", "libtransmission/torrent.h", "tests/libtransmission/block-info-test.cc", "tests/libtransmission/completion-test.cc", "tests/libtransmission/file-piece-map-test.cc", "tests/libtransmission/move-test.cc"], 
        )
    ])

@problem(
    id="transmission-cddd400",
    description="""
    test: fix race condition in rename-test (#2612)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="2410ad2fa69c097284df6ac8c73b3f2095a92fc1",
    test="cddd400f7e0d01a32fbaed889e9b39e7750d1ee9", 
    golden="cddd400f7e0d01a32fbaed889e9b39e7750d1ee9",
)
def transmission_cddd400(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="2410ad2fa69c097284df6ac8c73b3f2095a92fc1",
            test="cddd400f7e0d01a32fbaed889e9b39e7750d1ee9", 
            golden="cddd400f7e0d01a32fbaed889e9b39e7750d1ee9",
            jest_test_files=["libtransmission/verify.cc", "tests/libtransmission/test-fixtures.h"], 
        )
    ])

@problem(
    id="transmission-318d60b",
    description="""
    refactor: fix sonarcloud 'use enum class' code smells (#2590)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="a92af9193e1acb9f6f7a75a2b06fa0d925eb9ea7",
    test="318d60b72db870a263d2dbcf0fecd70107a3f439", 
    golden="318d60b72db870a263d2dbcf0fecd70107a3f439",
)
def transmission_318d60b(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="a92af9193e1acb9f6f7a75a2b06fa0d925eb9ea7",
            test="318d60b72db870a263d2dbcf0fecd70107a3f439", 
            golden="318d60b72db870a263d2dbcf0fecd70107a3f439",
            jest_test_files=["gtk/Application.cc", "gtk/HigWorkarea.h", "gtk/MainWindow.cc", "gtk/MakeDialog.cc", "gtk/PrefsDialog.h", "gtk/StatsDialog.cc", "gtk/TorrentCellRenderer.cc", "gtk/Utils.cc", "gtk/Utils.h", "libtransmission/announce-list.h", "libtransmission/makemeta.cc", "libtransmission/makemeta.h", "libtransmission/peer-msgs.cc", "libtransmission/resume.cc", "libtransmission/resume.h", "libtransmission/rpcimpl.cc", "libtransmission/torrent.cc", "macosx/CreatorWindowController.mm", "qt/Application.cc", "qt/FileTreeItem.cc", "qt/FileTreeItem.h", "qt/FileTreeModel.cc", "qt/MakeDialog.cc", "tests/libtransmission/rename-test.cc", "utils/create.cc"], 
        )
    ])

@problem(
    id="transmission-6f9cba4",
    description="""
    fixup! refactor: SAX-like benc parser pt. 1 (#2490) (#2544)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="0929d1a0131102c91bfbb38b869aeec6c7817076",
    test="6f9cba4088d5aaf29902e1b25ef0e0accd0a9829", 
    golden="6f9cba4088d5aaf29902e1b25ef0e0accd0a9829",
)
def transmission_6f9cba4(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="0929d1a0131102c91bfbb38b869aeec6c7817076",
            test="6f9cba4088d5aaf29902e1b25ef0e0accd0a9829", 
            golden="6f9cba4088d5aaf29902e1b25ef0e0accd0a9829",
            jest_test_files=["libtransmission/benc.h", "tests/libtransmission/benc-test.cc"], 
        )
    ])

@problem(
    id="transmission-8d75736",
    description="""
    fix: empty torrent filename (#2435)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="aa2183c9c5d25f6f06da31015e8c28243642b797",
    test="8d75736ad1b2c92f1cca04a24b60b8b226af96c8", 
    golden="8d75736ad1b2c92f1cca04a24b60b8b226af96c8",
)
def transmission_8d75736(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="aa2183c9c5d25f6f06da31015e8c28243642b797",
            test="8d75736ad1b2c92f1cca04a24b60b8b226af96c8", 
            golden="8d75736ad1b2c92f1cca04a24b60b8b226af96c8",
            jest_test_files=["libtransmission/resume.cc", "libtransmission/torrent-ctor.cc", "libtransmission/torrent-magnet.cc", "libtransmission/torrent-metainfo.h", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/transmission.h", "libtransmission/utils.cc", "macosx/Torrent.mm", "tests/libtransmission/rename-test.cc"], 
        )
    ])

@problem(
    id="transmission-2c09e99",
    description="""
    fix: parse utorrent peer-id version components as hex (#2411)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="be1e46383df3abdb07d892b48f81fd8d0dc2c3b8",
    test="2c09e99515b5b02f2220354f7d818ddd4eb052cd", 
    golden="2c09e99515b5b02f2220354f7d818ddd4eb052cd",
)
def transmission_2c09e99(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="be1e46383df3abdb07d892b48f81fd8d0dc2c3b8",
            test="2c09e99515b5b02f2220354f7d818ddd4eb052cd", 
            golden="2c09e99515b5b02f2220354f7d818ddd4eb052cd",
            jest_test_files=["libtransmission/clients.cc", "tests/libtransmission/clients-test.cc"], 
        )
    ])

@problem(
    id="transmission-41b2a80",
    description="""
    Fix another integer overflow bug on 32-bit platforms with torrents > 4GB (#2391)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b0ee4007ffee27b9fdcc685e377865dc6e8555c8",
    test="41b2a802cfac2c0131a5b5fb564b6c86d6e874a2", 
    golden="41b2a802cfac2c0131a5b5fb564b6c86d6e874a2",
)
def transmission_41b2a80(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b0ee4007ffee27b9fdcc685e377865dc6e8555c8",
            test="41b2a802cfac2c0131a5b5fb564b6c86d6e874a2", 
            golden="41b2a802cfac2c0131a5b5fb564b6c86d6e874a2",
            jest_test_files=["libtransmission/completion.cc", "tests/libtransmission/completion-test.cc"], 
        )
    ])

@problem(
    id="transmission-43b9d5c",
    description="""
    fix: potential infinite loop when parsing benc (#2389)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d2e840c64cfd99f72e0b2d15bd8e9edadbf939a9",
    test="43b9d5c147b3ef7587018904cb83dfb832c66b02", 
    golden="43b9d5c147b3ef7587018904cb83dfb832c66b02",
)
def transmission_43b9d5c(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d2e840c64cfd99f72e0b2d15bd8e9edadbf939a9",
            test="43b9d5c147b3ef7587018904cb83dfb832c66b02", 
            golden="43b9d5c147b3ef7587018904cb83dfb832c66b02",
            jest_test_files=["libtransmission/variant-benc.cc", "tests/libtransmission/variant-test.cc"], 
        )
    ])

@problem(
    id="transmission-0e321c2",
    description="""
    fix: clang warnings (#2339)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b62b8f28bf129810d767bc76502223201048b654",
    test="0e321c2d216bfc6e3994eae6c798eb7e1ec60b82", 
    golden="0e321c2d216bfc6e3994eae6c798eb7e1ec60b82",
)
def transmission_0e321c2(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b62b8f28bf129810d767bc76502223201048b654",
            test="0e321c2d216bfc6e3994eae6c798eb7e1ec60b82", 
            golden="0e321c2d216bfc6e3994eae6c798eb7e1ec60b82",
            jest_test_files=["libtransmission/crypto.cc", "libtransmission/crypto.h", "libtransmission/interned-string.h", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "tests/libtransmission/crypto-test.cc"], 
        )
    ])

@problem(
    id="transmission-e2be142",
    description="""
    fix: new warnings (#2270)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1bc10e3706a0c8c71f360fc3674bd662f8255118",
    test="e2be142ad643e583f222e14e5b9203af943468c5", 
    golden="e2be142ad643e583f222e14e5b9203af943468c5",
)
def transmission_e2be142(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1bc10e3706a0c8c71f360fc3674bd662f8255118",
            test="e2be142ad643e583f222e14e5b9203af943468c5", 
            golden="e2be142ad643e583f222e14e5b9203af943468c5",
            jest_test_files=["libtransmission/block-info.h", "libtransmission/torrent.h", "libtransmission/tr-utp.cc", "libtransmission/utils.cc", "libtransmission/variant.cc", "tests/libtransmission/metainfo-test.cc"], 
        )
    ])

@problem(
    id="transmission-b61b1e2",
    description="""
    test: add regression tests for transmission-show (#2255)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="ee83859bdc1cb2128b7c0d40aeda26b408ec3e8e",
    test="b61b1e2c1631f32a0372999e13fd366fa54da8dc", 
    golden="b61b1e2c1631f32a0372999e13fd366fa54da8dc",
)
def transmission_b61b1e2(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="ee83859bdc1cb2128b7c0d40aeda26b408ec3e8e",
            test="b61b1e2c1631f32a0372999e13fd366fa54da8dc", 
            golden="b61b1e2c1631f32a0372999e13fd366fa54da8dc",
            jest_test_files=["tests/CMakeLists.txt", "tests/utils/CMakeLists.txt", "tests/utils/assets/Inner_Sanctum_movie_archive.show", "tests/utils/assets/Inner_Sanctum_movie_archive.torrent", "tests/utils/assets/Thor_and_the_Amazon_Women.avi.show", "tests/utils/assets/Thor_and_the_Amazon_Women.avi.torrent", "tests/utils/assets/ubuntu-20.04.3-desktop-amd64.iso.show", "tests/utils/assets/ubuntu-20.04.3-desktop-amd64.iso.torrent", "tests/utils/run_transmission_show.cmake", "utils/show.cc"], 
        )
    ])

@problem(
    id="transmission-3d2fa18",
    description="""
    test: improve tr_bitfield and tr_block_info coverage (#2226)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="de169c7ec37e017e0a8dfb1422b599e08e40f527",
    test="3d2fa18c613bb0ce912280ad95f486d69a4078ae", 
    golden="3d2fa18c613bb0ce912280ad95f486d69a4078ae",
)
def transmission_3d2fa18(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="de169c7ec37e017e0a8dfb1422b599e08e40f527",
            test="3d2fa18c613bb0ce912280ad95f486d69a4078ae", 
            golden="3d2fa18c613bb0ce912280ad95f486d69a4078ae",
            jest_test_files=["libtransmission/bitfield.cc", "libtransmission/block-info.cc", "tests/libtransmission/bitfield-test.cc", "tests/libtransmission/block-info-test.cc"], 
        )
    ])

@problem(
    id="transmission-dbd9130",
    description="""
    fix: env var leak in tr_spawn_async() (#2212)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="d4e0f368c8c0ce7bc13d79a234cf398d7c85b1e2",
    test="dbd9130d9df3b2b0ebf4e7e003fc0e1f0f8d9263", 
    golden="dbd9130d9df3b2b0ebf4e7e003fc0e1f0f8d9263",
)
def transmission_dbd9130(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="d4e0f368c8c0ce7bc13d79a234cf398d7c85b1e2",
            test="dbd9130d9df3b2b0ebf4e7e003fc0e1f0f8d9263", 
            golden="dbd9130d9df3b2b0ebf4e7e003fc0e1f0f8d9263",
            jest_test_files=["libtransmission/subprocess-posix.cc", "libtransmission/subprocess-win32.cc", "libtransmission/subprocess.h", "libtransmission/torrent.cc", "tests/libtransmission/subprocess-test.cc"], 
        )
    ])

@problem(
    id="transmission-617df25",
    description="""
    fix: coverity regression reported on 2021-11-17
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="f14e741052068b00305f4baf088934cad9b6e683",
    test="617df25ba184defb9541dccfe1cd3bc9dd107985", 
    golden="617df25ba184defb9541dccfe1cd3bc9dd107985",
)
def transmission_617df25(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="f14e741052068b00305f4baf088934cad9b6e683",
            test="617df25ba184defb9541dccfe1cd3bc9dd107985", 
            golden="617df25ba184defb9541dccfe1cd3bc9dd107985",
            jest_test_files=["tests/libtransmission/metainfo-test.cc"], 
        )
    ])

@problem(
    id="transmission-ec94c90",
    description="""
    fix: coverity warnings (#2186)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1ba81938bf93512f8644cf38acaae8d9574f4851",
    test="ec94c90da9ba1c5a1c58453e55d38e54a5dc6d04", 
    golden="ec94c90da9ba1c5a1c58453e55d38e54a5dc6d04",
)
def transmission_ec94c90(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1ba81938bf93512f8644cf38acaae8d9574f4851",
            test="ec94c90da9ba1c5a1c58453e55d38e54a5dc6d04", 
            golden="ec94c90da9ba1c5a1c58453e55d38e54a5dc6d04",
            jest_test_files=["gtk/Prefs.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "tests/libtransmission/metainfo-test.cc", "tests/libtransmission/subprocess-test.cc"], 
        )
    ])

@problem(
    id="transmission-60b802a",
    description="""
    refactor: fix some msvc compiler warnings (#2185)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="0fba4769170b9b4aa894e7f13dfd257534eb95b6",
    test="60b802a22b7eaddea2412d5098cbd0d52c25ef7b", 
    golden="60b802a22b7eaddea2412d5098cbd0d52c25ef7b",
)
def transmission_60b802a(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="0fba4769170b9b4aa894e7f13dfd257534eb95b6",
            test="60b802a22b7eaddea2412d5098cbd0d52c25ef7b", 
            golden="60b802a22b7eaddea2412d5098cbd0d52c25ef7b",
            jest_test_files=["libtransmission/announcer.cc", "libtransmission/utils.cc", "tests/libtransmission/rename-test.cc"], 
        )
    ])

@problem(
    id="transmission-af8e9e6",
    description="""
    fixup! refactor: rpc-server.cc (#2152) (#2164)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="8980a33f4a46e036a8e00979f9a05a9759be13b9",
    test="af8e9e66b9ba0e0504d140712a10777d40f8befe", 
    golden="af8e9e66b9ba0e0504d140712a10777d40f8befe",
)
def transmission_af8e9e6(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="8980a33f4a46e036a8e00979f9a05a9759be13b9",
            test="af8e9e66b9ba0e0504d140712a10777d40f8befe", 
            golden="af8e9e66b9ba0e0504d140712a10777d40f8befe",
            jest_test_files=["libtransmission/crypto-utils.cc", "libtransmission/crypto-utils.h", "libtransmission/rpc-server.cc", "libtransmission/rpc-server.h", "libtransmission/transmission.h", "tests/libtransmission/session-test.cc"], 
        )
    ])

@problem(
    id="transmission-af4a953",
    description="""
    fixup! refactor: remove tr_piece struct (#2059) (#2115)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="2bd328c0826a0ed1c6c21ea2514ee78ba569235a",
    test="af4a953cd1556f9d6fc1dd799b16a9d2d43a9a7e", 
    golden="af4a953cd1556f9d6fc1dd799b16a9d2d43a9a7e",
)
def transmission_af4a953(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="2bd328c0826a0ed1c6c21ea2514ee78ba569235a",
            test="af4a953cd1556f9d6fc1dd799b16a9d2d43a9a7e", 
            golden="af4a953cd1556f9d6fc1dd799b16a9d2d43a9a7e",
            jest_test_files=["libtransmission/bitfield.cc", "libtransmission/bitfield.h", "libtransmission/peer-msgs.cc", "libtransmission/resume.cc", "tests/libtransmission/bitfield-test.cc"], 
        )
    ])

@problem(
    id="transmission-3008a99",
    description="""
    fix: Bitfield.getRaw() regression (#2023)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="62c92227e3e30e25d37f18195cc8c08562939026",
    test="3008a992ca4c9cf138d482a7c3cb0706e062d277", 
    golden="3008a992ca4c9cf138d482a7c3cb0706e062d277",
)
def transmission_3008a99(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="62c92227e3e30e25d37f18195cc8c08562939026",
            test="3008a992ca4c9cf138d482a7c3cb0706e062d277", 
            golden="3008a992ca4c9cf138d482a7c3cb0706e062d277",
            jest_test_files=["libtransmission/bitfield.cc", "libtransmission/bitfield.h", "libtransmission/completion.cc", "libtransmission/completion.h", "libtransmission/peer-common.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/resume.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/span.h", "libtransmission/torrent.cc", "libtransmission/webseed.cc", "tests/libtransmission/bitfield-test.cc"], 
        )
    ])

@problem(
    id="transmission-8c40fd8",
    description="""
    Fix testing against reference crypto impl
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="1413346fa2634c7ba21bd15d8f86f6fa66f480c8",
    test="8c40fd8b39f7591705f461b18b87df051461177b", 
    golden="8c40fd8b39f7591705f461b18b87df051461177b",
)
def transmission_8c40fd8(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="1413346fa2634c7ba21bd15d8f86f6fa66f480c8",
            test="8c40fd8b39f7591705f461b18b87df051461177b", 
            golden="8c40fd8b39f7591705f461b18b87df051461177b",
            jest_test_files=["tests/libtransmission/crypto-test-ref.h"], 
        )
    ])

@problem(
    id="transmission-94ee81f",
    description="""
    fixup! refactor: add tr_peer_id_t (#2004) (#2016)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="0c39924074a83dfb09343e34423e1908d54abd2a",
    test="94ee81f98d8bd08ecd8bc292fb6661d896f4089a", 
    golden="94ee81f98d8bd08ecd8bc292fb6661d896f4089a",
)
def transmission_94ee81f(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="0c39924074a83dfb09343e34423e1908d54abd2a",
            test="94ee81f98d8bd08ecd8bc292fb6661d896f4089a", 
            golden="94ee81f98d8bd08ecd8bc292fb6661d896f4089a",
            jest_test_files=["libtransmission/clients.cc", "libtransmission/clients.h", "libtransmission/handshake.cc", "libtransmission/peer-mgr.cc", "tests/libtransmission/clients-test.cc"], 
        )
    ])

@problem(
    id="transmission-4aba9b6",
    description="""
    fix: assertion failure in bitfield::bitfield(flags, n) (#1976)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="de7b7a284ce75f77c6af509c6827680ca8b5b970",
    test="4aba9b623f1eda0a24cc8ab11efa7fc02b5acbd9", 
    golden="4aba9b623f1eda0a24cc8ab11efa7fc02b5acbd9",
)
def transmission_4aba9b6(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="de7b7a284ce75f77c6af509c6827680ca8b5b970",
            test="4aba9b623f1eda0a24cc8ab11efa7fc02b5acbd9", 
            golden="4aba9b623f1eda0a24cc8ab11efa7fc02b5acbd9",
            jest_test_files=["libtransmission/bitfield.cc", "tests/libtransmission/bitfield-test.cc"], 
        )
    ])

@problem(
    id="transmission-953f073",
    description="""
    Modernize bitfield.cc: Storage changes and refactor (#1927)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="43ad1346eb5fa0a9a3f3479ff0bd8fa44c684f83",
    test="953f07375aae3a0d46231ce02f2c9b0588cf72f4", 
    golden="953f07375aae3a0d46231ce02f2c9b0588cf72f4",
)
def transmission_953f073(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="43ad1346eb5fa0a9a3f3479ff0bd8fa44c684f83",
            test="953f07375aae3a0d46231ce02f2c9b0588cf72f4", 
            golden="953f07375aae3a0d46231ce02f2c9b0588cf72f4",
            jest_test_files=["libtransmission/bitfield.cc", "libtransmission/bitfield.h", "libtransmission/completion.cc", "libtransmission/completion.h", "libtransmission/peer-msgs.cc", "libtransmission/resume.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "libtransmission/span.h", "libtransmission/torrent.h", "libtransmission/tr-assert.h", "libtransmission/transmission.h", "libtransmission/utils.cc", "libtransmission/webseed.cc", "tests/libtransmission/bitfield-test.cc"], 
        )
    ])

@problem(
    id="transmission-fb39c46",
    description="""
    Fix/benc zero length dict key (#1964)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="23d85458f83d979475e5ed0db4446aee04f7e590",
    test="fb39c4663c9e6b7fadc7cd55bdcfa04167ae53f1", 
    golden="fb39c4663c9e6b7fadc7cd55bdcfa04167ae53f1",
)
def transmission_fb39c46(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="23d85458f83d979475e5ed0db4446aee04f7e590",
            test="fb39c4663c9e6b7fadc7cd55bdcfa04167ae53f1", 
            golden="fb39c4663c9e6b7fadc7cd55bdcfa04167ae53f1",
            jest_test_files=["libtransmission/variant-benc.cc", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/assets/Android-x86 8.1 r6 iso.torrent", "tests/libtransmission/metainfo-test.cc"], 
        )
    ])

@problem(
    id="transmission-916d418",
    description="""
    fix: some Coverity regressions reported on 2021-09-16 (#1870)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="b546fd423fd3af7ad061d0cdc39b5e03a487509b",
    test="916d418824586fd4f11d57356410492f779547b4", 
    golden="916d418824586fd4f11d57356410492f779547b4",
)
def transmission_916d418(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="b546fd423fd3af7ad061d0cdc39b5e03a487509b",
            test="916d418824586fd4f11d57356410492f779547b4", 
            golden="916d418824586fd4f11d57356410492f779547b4",
            jest_test_files=["tests/libtransmission/blocklist-test.cc", "tests/libtransmission/copy-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/subprocess-test.cc", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-312d182",
    description="""
    C++ modernize: Replace MIN/MAX with type safe std::min/std::max (#1806)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="6aba12888acf34b84faa6661a627ac751f352f51",
    test="312d18281dbec9eb5e64a94fca946a1a5fc0d69d", 
    golden="312d18281dbec9eb5e64a94fca946a1a5fc0d69d",
)
def transmission_312d182(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="6aba12888acf34b84faa6661a627ac751f352f51",
            test="312d18281dbec9eb5e64a94fca946a1a5fc0d69d", 
            golden="312d18281dbec9eb5e64a94fca946a1a5fc0d69d",
            jest_test_files=["daemon/daemon-win32.c", "libtransmission/announcer.cc", "libtransmission/bandwidth.cc", "libtransmission/bitfield.cc", "libtransmission/fdlimit.cc", "libtransmission/file-posix.cc", "libtransmission/file.cc", "libtransmission/inout.cc", "libtransmission/makemeta.cc", "libtransmission/peer-io.cc", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/port-forwarding.cc", "libtransmission/ptrarray.cc", "libtransmission/quark.cc", "libtransmission/resume.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/session.cc", "libtransmission/subprocess-win32.cc", "libtransmission/torrent.cc", "libtransmission/tr-dht.cc", "libtransmission/tr-getopt.cc", "libtransmission/tr-lpd.cc", "libtransmission/tr-macros.h", "libtransmission/utils.cc", "libtransmission/verify.cc", "libtransmission/web.cc", "libtransmission/webseed.cc", "tests/libtransmission/copy-test.cc"], 
        )
    ])

@problem(
    id="transmission-43d1ece",
    description="""
    C++ modernization: Replace NULLs with typesafe nullptrs (#1799)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="098c7508e37483d6ac0d413d90331ff4a2ead092",
    test="43d1ece5629b50e6cad3c224fb4eca6a20510951", 
    golden="43d1ece5629b50e6cad3c224fb4eca6a20510951",
)
def transmission_43d1ece(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="098c7508e37483d6ac0d413d90331ff4a2ead092",
            test="43d1ece5629b50e6cad3c224fb4eca6a20510951", 
            golden="43d1ece5629b50e6cad3c224fb4eca6a20510951",
            jest_test_files=["libtransmission/announcer-http.cc", "libtransmission/announcer-udp.cc", "libtransmission/announcer.cc", "libtransmission/bandwidth.cc", "libtransmission/bandwidth.h", "libtransmission/bitfield.cc", "libtransmission/blocklist.cc", "libtransmission/cache.cc", "libtransmission/clients.cc", "libtransmission/crypto-utils-cyassl.cc", "libtransmission/crypto-utils-fallback.cc", "libtransmission/crypto-utils-openssl.cc", "libtransmission/crypto-utils-polarssl.cc", "libtransmission/crypto-utils.cc", "libtransmission/crypto.cc", "libtransmission/error.cc", "libtransmission/fdlimit.cc", "libtransmission/file-posix.cc", "libtransmission/file-win32.cc", "libtransmission/file.cc", "libtransmission/file.h", "libtransmission/handshake.cc", "libtransmission/inout.cc", "libtransmission/jsonsl.h", "libtransmission/list.cc", "libtransmission/log.cc", "libtransmission/magnet.cc", "libtransmission/makemeta.cc", "libtransmission/metainfo.cc", "libtransmission/natpmp.cc", "libtransmission/net.cc", "libtransmission/net.h", "libtransmission/peer-io.cc", "libtransmission/peer-io.h", "libtransmission/peer-mgr.cc", "libtransmission/peer-msgs.cc", "libtransmission/platform-quota.cc", "libtransmission/platform.cc", "libtransmission/port-forwarding.cc", "libtransmission/ptrarray.cc", "libtransmission/ptrarray.h", "libtransmission/quark.cc", "libtransmission/resume.cc", "libtransmission/rpc-server.cc", "libtransmission/rpcimpl.cc", "libtransmission/session-id.cc", "libtransmission/session.cc", "libtransmission/session.h", "libtransmission/stats.cc", "libtransmission/subprocess-posix.cc", "libtransmission/subprocess-win32.cc", "libtransmission/torrent-ctor.cc", "libtransmission/torrent-magnet.cc", "libtransmission/torrent.cc", "libtransmission/torrent.h", "libtransmission/tr-dht.cc", "libtransmission/tr-getopt.cc", "libtransmission/tr-lpd.cc", "libtransmission/tr-udp.cc", "libtransmission/tr-utp.cc", "libtransmission/trevent.cc", "libtransmission/upnp.cc", "libtransmission/utils.cc", "libtransmission/variant-benc.cc", "libtransmission/variant-json.cc", "libtransmission/variant.cc", "libtransmission/verify.cc", "libtransmission/watchdir-generic.cc", "libtransmission/watchdir-inotify.cc", "libtransmission/watchdir-kqueue.cc", "libtransmission/watchdir-win32.cc", "libtransmission/watchdir.cc", "libtransmission/web.cc", "libtransmission/webseed.cc", "tests/libtransmission/subprocess-test-program.cc"], 
        )
    ])

@problem(
    id="transmission-a459e5e",
    description="""
    Switch to a standalone ARC4 implementation (#1788)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="97a6f1232ed8759f05db9d82d2b2c246d5c23811",
    test="a459e5e11b2d2524b649f7487368de30c8d2af21", 
    golden="a459e5e11b2d2524b649f7487368de30c8d2af21",
)
def transmission_a459e5e(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="97a6f1232ed8759f05db9d82d2b2c246d5c23811",
            test="a459e5e11b2d2524b649f7487368de30c8d2af21", 
            golden="a459e5e11b2d2524b649f7487368de30c8d2af21",
            jest_test_files=[".gitmodules", "CMakeLists.txt", "Transmission.xcodeproj/project.pbxproj", "libtransmission/CMakeLists.txt", "libtransmission/crypto-utils-cyassl.c", "libtransmission/crypto-utils-openssl.c", "libtransmission/crypto-utils-polarssl.c", "libtransmission/crypto-utils.c", "libtransmission/crypto-utils.h", "libtransmission/crypto.c", "libtransmission/crypto.h", "tests/libtransmission/crypto-test-ref.h", "third-party/arc4"], 
        )
    ])

@problem(
    id="transmission-c0ed825",
    description="""
    perf: lookup tables for faster torrent searching. (#1778)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="696b0bcab95a17a83ea2ebc31044ea5ff1755d9c",
    test="c0ed82533cf8f48c79c4efe86988c81c930b46a1", 
    golden="c0ed82533cf8f48c79c4efe86988c81c930b46a1",
)
def transmission_c0ed825(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="696b0bcab95a17a83ea2ebc31044ea5ff1755d9c",
            test="c0ed82533cf8f48c79c4efe86988c81c930b46a1", 
            golden="c0ed82533cf8f48c79c4efe86988c81c930b46a1",
            jest_test_files=["libtransmission/session.c", "libtransmission/session.h", "libtransmission/torrent.c", "tests/libtransmission/.clang-tidy"], 
        )
    ])

@problem(
    id="transmission-0155252",
    description="""
    Add in-kernel file copying for several platforms. (#1092)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="af3a4d45578dc8511fd2f26636ae727a728b65e0",
    test="0155252823d71576f2d1bdcbc301d2e6006cf7f5", 
    golden="0155252823d71576f2d1bdcbc301d2e6006cf7f5",
)
def transmission_0155252(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="af3a4d45578dc8511fd2f26636ae727a728b65e0",
            test="0155252823d71576f2d1bdcbc301d2e6006cf7f5", 
            golden="0155252823d71576f2d1bdcbc301d2e6006cf7f5",
            jest_test_files=["CMakeLists.txt", "libtransmission/file-posix.c", "libtransmission/file-win32.c", "libtransmission/file.h", "libtransmission/utils.c", "tests/libtransmission/CMakeLists.txt", "tests/libtransmission/copy-test.cc"], 
        )
    ])

@problem(
    id="transmission-f59118d",
    description="""
    feat: add torrent-get 'primary-mime-type' to RPC. (#1464)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="4c7153fa48d86627af3a0ec4e1369632c81484d0",
    test="f59118d1fe6a320d797b151a6f235f739ef3b487", 
    golden="f59118d1fe6a320d797b151a6f235f739ef3b487",
)
def transmission_f59118d(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="4c7153fa48d86627af3a0ec4e1369632c81484d0",
            test="f59118d1fe6a320d797b151a6f235f739ef3b487", 
            golden="f59118d1fe6a320d797b151a6f235f739ef3b487",
            jest_test_files=["Transmission.xcodeproj/project.pbxproj", "extras/rpc-spec.txt", "libtransmission/CMakeLists.txt", "libtransmission/mime-types.c", "libtransmission/mime-types.h", "libtransmission/mime-types.js", "libtransmission/quark.c", "libtransmission/quark.h", "libtransmission/rpcimpl.c", "libtransmission/torrent.c", "libtransmission/torrent.h", "libtransmission/utils.c", "libtransmission/utils.h", "qt/IconCache.cc", "qt/IconCache.h", "qt/Session.cc", "qt/Torrent.cc", "qt/Torrent.h", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-c2fb393",
    description="""
    chore: fix clang-tidy-11 warnings (#1436)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="bda60c5a18a885cfc3543cc596a0b4756e3936b4",
    test="c2fb3933905e36f63b963f06095719ac2059bb7d", 
    golden="c2fb3933905e36f63b963f06095719ac2059bb7d",
)
def transmission_c2fb393(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="bda60c5a18a885cfc3543cc596a0b4756e3936b4",
            test="c2fb3933905e36f63b963f06095719ac2059bb7d", 
            golden="c2fb3933905e36f63b963f06095719ac2059bb7d",
            jest_test_files=["qt/Application.h", "qt/DetailsDialog.h", "qt/FileTreeModel.h", "qt/Formatter.cc", "qt/IconCache.cc", "qt/OptionsDialog.h", "qt/Prefs.cc", "qt/Prefs.h", "qt/RelocateDialog.cc", "qt/RpcClient.cc", "qt/RpcQueue.cc", "qt/RpcQueue.h", "qt/Session.h", "qt/TorrentDelegate.cc", "qt/TorrentDelegate.h", "qt/TorrentModel.h", "qt/TrackerDelegate.cc", "tests/libtransmission/.clang-tidy"], 
        )
    ])

@problem(
    id="transmission-ce51f1a",
    description="""
    refactor: work around msvc constxpr std::array bug (#1429)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="9f7c8654549e8deeb434c9f653e31d6900acdc00",
    test="ce51f1adbfa97e026801efacaadd520a6e792c7d", 
    golden="ce51f1adbfa97e026801efacaadd520a6e792c7d",
)
def transmission_ce51f1a(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="9f7c8654549e8deeb434c9f653e31d6900acdc00",
            test="ce51f1adbfa97e026801efacaadd520a6e792c7d", 
            golden="ce51f1adbfa97e026801efacaadd520a6e792c7d",
            jest_test_files=["tests/libtransmission/clients-test.cc", "tests/libtransmission/crypto-test.cc", "tests/libtransmission/getopt-test.cc", "tests/libtransmission/magnet-test.cc", "tests/libtransmission/metainfo-test.cc", "tests/libtransmission/rename-test.cc", "tests/libtransmission/rpc-test.cc", "tests/libtransmission/utils-test.cc"], 
        )
    ])

@problem(
    id="transmission-8445e09",
    description="""
    Fix: Test structure shadowing Google Test suite one (#1417)
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    """,
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="90ce7efc09c5d7fb562d74e66da61f606f610f12",
    test="8445e090a72cc5e1cd63002d46b3e24ddceed583", 
    golden="8445e090a72cc5e1cd63002d46b3e24ddceed583",
)
def transmission_8445e09(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="90ce7efc09c5d7fb562d74e66da61f606f610f12",
            test="8445e090a72cc5e1cd63002d46b3e24ddceed583", 
            golden="8445e090a72cc5e1cd63002d46b3e24ddceed583",
            jest_test_files=["tests/libtransmission/clients-test.cc", "tests/libtransmission/crypto-test.cc", "tests/libtransmission/file-test.cc", "tests/libtransmission/metainfo-test.cc", "tests/libtransmission/variant-test.cc"], 
        )
    ])
