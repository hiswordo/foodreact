chrome.webNavigation.onHistoryStateUpdated.addListener(
  data => {
    chrome.tabs.get(data.tabId, () => {
      chrome.tabs.executeScript(data.tabId, {
        code: 'if(typeof addButton !== "undefined") {addButton()}',
        runAt: 'document_start',
      });
    });
  },
  { url: [{ hostSuffix: '.youtube.com' }] }
);
