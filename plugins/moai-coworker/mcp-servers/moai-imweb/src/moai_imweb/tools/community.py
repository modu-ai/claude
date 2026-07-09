"""Generated tools — Community (커뮤니티 (폼/Q&A/구매평)). DO NOT EDIT; regenerate via tools/_generator.py."""
from __future__ import annotations

from typing import Literal

from .._app import mcp
from .._base import get_client

# action -> (method, path, path_params, query_params, has_body)
_OPS: dict[str, tuple] = {
    'read_all_forms': ('GET', '/community/forms', [], ['page', 'limit', 'unitCode', 'formCreateTimeType', 'formCreateTime', 'formEditTimeType', 'formEditTime'], False),
    'read_one_form': ('GET', '/community/forms/{formNo}', ['formNo'], ['unitCode'], False),
    'read_all_form_submissions': ('GET', '/community/form-submissions', [], ['page', 'limit', 'unitCode', 'formNo', 'formSubmitTimeType', 'formSubmitTime'], False),
    'read_one_form_submission': ('GET', '/community/form-submissions/{submitCode}', ['submitCode'], ['unitCode'], False),
    'read_all_site_qna': ('GET', '/community/qna', [], ['page', 'limit', 'prodCode', 'status', 'qnaCreateTimeType', 'qnaCreateTime'], False),
    'create_site_qna_reply': ('POST', '/community/qna', [], [], True),
    'read_site_qna_answer': ('GET', '/community/qna-answer', [], ['qnaNoList'], False),
    'read_one_site_qna_by_idx': ('GET', '/community/qna/{qnaNo}', ['qnaNo'], [], False),
    'read_all_site_review': ('GET', '/community/review', [], ['page', 'limit', 'prodNo', 'level', 'rating', 'isPhoto', 'reviewCreateTimeType', 'reviewCreateTime'], False),
    'create_site_review': ('POST', '/community/review', [], [], True),
    'read_one_site_review': ('GET', '/community/review/{reviewNo}', ['reviewNo'], [], False),
    'update_site_review_by_review_no': ('PUT', '/community/review/{reviewNo}', ['reviewNo'], [], True),
    'delete_site_review_by_review_no': ('DELETE', '/community/review/{reviewNo}', ['reviewNo'], [], False),
    'read_site_review_answer': ('GET', '/community/review-answer', [], ['reviewNoList'], False),
    'create_site_review_answer': ('POST', '/community/review-answer', [], [], True),
    'delete_site_review_answer_by_review_no': ('DELETE', '/community/review-answer/{reviewAnswerNo}', ['reviewAnswerNo'], [], False),
    'read_all_site_review_by_cursor': ('GET', '/community/review/cursor', [], ['cursor', 'direction', 'limit', 'prodNo', 'level', 'rating', 'isPhoto', 'reviewCreateTimeType', 'reviewCreateTime'], False),
}

@mcp.tool()
def imweb_community(action: Literal["read_all_forms", "read_one_form", "read_all_form_submissions", "read_one_form_submission", "read_all_site_qna", "create_site_qna_reply", "read_site_qna_answer", "read_one_site_qna_by_idx", "read_all_site_review", "create_site_review", "read_one_site_review", "update_site_review_by_review_no", "delete_site_review_by_review_no", "read_site_review_answer", "create_site_review_answer", "delete_site_review_answer_by_review_no", "read_all_site_review_by_cursor"], params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:
    r"""커뮤니티 (폼/Q&A/구매평) 도구 — 17개 action 을 디스패치합니다.

Args:
    action: 수행 작업 키 (아래 17개 중 하나).
    params: path + query 파라미터 딕셔너리. 예: {"orderNo": "ORD123", "page": 1}
    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.
    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).

Actions:
    - read_all_forms: 입력폼 목록 조회 [GET /community/forms query=['page', 'limit', 'unitCode', 'formCreateTimeType', 'formCreateTime', 'formEditTimeType', 'formEditTime']]
    - read_one_form: 입력폼 상세 조회 [GET /community/forms/{formNo} path=['formNo'] query=['unitCode']]
    - read_all_form_submissions: 입력폼 제출 목록 조회 [GET /community/form-submissions query=['page', 'limit', 'unitCode', 'formNo', 'formSubmitTimeType', 'formSubmitTime']]
    - read_one_form_submission: 입력폼 제출 상세 조회 [GET /community/form-submissions/{submitCode} path=['submitCode'] query=['unitCode']]
    - read_all_site_qna: Q&A 목록 조회 [GET /community/qna query=['page', 'limit', 'prodCode', 'status', 'qnaCreateTimeType', 'qnaCreateTime']]
    - create_site_qna_reply: Q&A 답변 등록 [POST /community/qna  [body]]
    - read_site_qna_answer: Q&A 답글 목록 조회 [GET /community/qna-answer query=['qnaNoList']]
    - read_one_site_qna_by_idx: Q&A 조회 [GET /community/qna/{qnaNo} path=['qnaNo']]
    - read_all_site_review: 구매평 목록 조회 [GET /community/review query=['page', 'limit', 'prodNo', 'level', 'rating', 'isPhoto', 'reviewCreateTimeType', 'reviewCreateTime']]
    - create_site_review: 구매평 작성 [POST /community/review  [body]]
    - read_one_site_review: 구매평 조회 [GET /community/review/{reviewNo} path=['reviewNo']]
    - update_site_review_by_review_no: 구매평 수정 [PUT /community/review/{reviewNo} path=['reviewNo']  [body]]
    - delete_site_review_by_review_no: 구매평 삭제 [DELETE /community/review/{reviewNo} path=['reviewNo']]
    - read_site_review_answer: 구매평 답글 목록 조회 [GET /community/review-answer query=['reviewNoList']]
    - create_site_review_answer: 구매평 답글 등록 [POST /community/review-answer  [body]]
    - delete_site_review_answer_by_review_no: 구매평 답글 삭제 [DELETE /community/review-answer/{reviewAnswerNo} path=['reviewAnswerNo']]
    - read_all_site_review_by_cursor: 구매평 목록 조회 (커서 기반) [GET /community/review/cursor query=['cursor', 'direction', 'limit', 'prodNo', 'level', 'rating', 'isPhoto', 'reviewCreateTimeType', 'reviewCreateTime']]

Body schemas:
  [create_site_qna_reply]
    body (CreateSiteQnaReplyRequestDto):
      - qnaNo (float 필수): 답변할 Q&A 번호
      - reply (str 필수): Q&A 답변 내용
      - memberUid (str 필수): Q&A 답변 작성자 아이디
  [create_site_review]
    body (CreateSiteReviewRequestDto):
      - unitCode (str 필수): 유닛코드
      - prodNo (float 필수): 상품번호
      - body (str 필수): 구매평 내용
      - nick (str 필수): 작성자 이름
      - wtime (str 필수): 작성 시각 (ISO 8601 형식). 현재 시각 이후(미래)의 값은 허용되지 않습니다.
      - rating (float 필수): 평점 (1~5점)
      - memberUid (str): 회원 ID
      - isHide (str): 숨김 여부
      - grade (str): 구매평 등급 (1-워스트, 2-일반, 3-베스트)
      - prodOption (str): 구매한 상품 옵션 명
      - orderItemCode (str): 주문 아이템 코드
      - originReviewId (str): 원본 리뷰 ID
      - images (list): 리뷰 이미지 파일 (선택, 최대 20개)
  [update_site_review_by_review_no]
    body (UpdateSiteReviewRequestDto):
      - body (str): 구매평 내용
      - rating (float): 구매평 평점
  [create_site_review_answer]
    body (CreateSiteReviewAnswerRequestDto):
      - reviewNo (float 필수): 답글을 작성할 구매평 번호
      - unitCode (str 필수): 유닛코드
      - body (str 필수): 구매평 답글 내용
      - nick (str 필수): 작성자 이름
      - wtime (str 필수): 작성 시각 (ISO 8601, UTC). 현재 시각 이후(미래)의 값은 허용되지 않습니다.
      - memberUid (str): 회원 ID
      - originReviewId (str): 원본 리뷰 ID

Returns: API JSON."""
    _method, _path, _pp, _qp, _has_body = _OPS[action]
    _params = params or {}
    _pp_val = {k: _params[k] for k in _pp if k in _params}
    _qp_val = {k: _params[k] for k in _qp if k in _params}
    _client = get_client()
    if paginate and _method == "GET":
        return _client.list_all_pages(_path, params=_qp_val or None)
    _kw = {}
    if _pp_val:
        _kw["path_params"] = _pp_val
    if _qp_val:
        _kw["params"] = _qp_val
    if _has_body:
        _kw["json_body"] = body or {}
    return _client.request(_method, _path, **_kw)

