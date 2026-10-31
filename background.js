const BRIDGE = "http://127.0.0.1:8765";

chrome.runtime.onInstalled.addListener(() => {
  console.info("RoPilot installed. Local bridge:", BRIDGE);
});

async function getBridgeHealth() {
  try {
    const response = await fetch(`${BRIDGE}/health`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    return { ok: false, error: String(error) };
  }
}

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message?.type === "ROPILOT_HEALTH") {
    getBridgeHealth().then(sendResponse);
    return true;
  }
});
