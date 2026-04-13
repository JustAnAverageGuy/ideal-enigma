import http from 'http';

const judgeView = { extensionToJudgeViewMessage: (message) => { globalThis.logger.log("View got message ", message); } }

const getJudgeViewProvider = () => judgeView

const emptyResponse = { empty: true, }
const savedResponseWithProblem = {
    url: '',
    empty: false,
    problemName: "2123A",
    sourceCode: "print('Hello Bitches')",
    languageId: 70,
}

const globalThis = { logger: { log: (...args) => { console.log(new Date().toLocaleString(),'|',...args) } } }
const vscode = { window: { showErrorMessage: globalThis.logger.log } }

const COMPANION_LOGGING = true;

const handleNewProblem = (problem) => {
    // console.log("Handling Problem: ", problem);
    globalThis.logger.log("Handling Problem: ", problem);
}

let savedResponse = emptyResponse;

const server = http.createServer((req, res) => {
    const { headers } = req;
    let rawProblem = '';

    req.on('data', (chunk) => {
        COMPANION_LOGGING &&
            globalThis.logger.log('Companion server got data');
        rawProblem += chunk;
    });
    req.on('close', function() {
        try {
            if (rawProblem == '') {
                return;
            }
            const problem = JSON.parse(rawProblem);
            handleNewProblem(problem);
            COMPANION_LOGGING &&
                globalThis.logger.log(
                    'Companion server closed connection.',
                );
        } catch (e) {
            vscode.window.showErrorMessage(
                `Error parsing problem from companion "${e}. Raw problem: '${rawProblem}'"`,
            );
        }
    });
    res.write(JSON.stringify(savedResponse));
    if (headers['cph-submit'] == 'true') {
        COMPANION_LOGGING &&
            globalThis.logger.log(
                'Request was from the cph-submit extension; sending savedResponse and clearing it',
                savedResponse,
            );

        if (savedResponse.empty != true) {
            getJudgeViewProvider().extensionToJudgeViewMessage({
                command: 'submit-finished',
            });
        }
        savedResponse = emptyResponse;
    }
    res.end();
});

server.on('error', (err) => {
   globalThis.logger.log('Error Received', err.message, err)
})

server.listen(27121);

setTimeout(() => {
    globalThis.logger.log('setting up savedResponse to have problem content');
    savedResponse = savedResponseWithProblem;
    globalThis.logger.log('set up ');
    globalThis.logger.log(savedResponse);
},10000)
