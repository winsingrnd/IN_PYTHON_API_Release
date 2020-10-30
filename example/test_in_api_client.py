#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python Module

import sys
import inspect
from pprint import pprint
import collections
import unittest


# IN Python Module
from IN_API_CLIENT import InApiClient
from IN_API_CLIENT import printer
import IN_DATA_STRUCTURE
import IN_STREAMING
import IN_COMMON

# 你可能用到的一些 Enum 的结构体
from IN_DATA_STRUCTURE import TagObjectID, BusFileType, TaskFileType, FileStatus, CommentType, TaskStatus, PipelineType




# ---------------------- 需要添加本项目路径 ----------------------------
# 如果 3rd_party_plugins 和 Launch Tool 里已添加路径可不加
# 在外部运行时, 需要添加本项目的路径,
# 如果你没有 requests 的一些包, 也需要添加 3rd 里的路径

# sys.path.append(r"C:\test_3rd_party_plugins\site-packages\IN_PYTHON_API_Release\src")
# sys.path.append(r"C:\test_3rd_party_plugins\site-packages\python27")



# ---------------------- 需要先启动 Server ----------------------------
# 你可以在任何地方启动/停止 Server, 整个本地只会使用一个 Server
# 运行 Server 需要用到我们提供的 env 里的 python.exe, Client 则不需要

# Server 和 Client 能在外部分开单独运行


# ------ 在 DCC 外, 添加了 sys 路径后, 可直接开启 Server ------
# import IN_API_SERVER
# server = IN_API_SERVER.run_server()



# ------ 在 DCC 里可运行以下命令 启动/停止 Server ------
# import IN_API_SERVER_MANAGER

# print("prepare: {}".format(IN_API_SERVER_MANAGER.prepare_server()))

# servers = IN_API_SERVER_MANAGER.check_server()
# print('servers:', servers)
# if not servers:
#     assert IN_API_SERVER_MANAGER.start_server() is True


# -------------------- 注意 --------------------
# 在结束的时候使用 stop_server
# 或者在更新之后注意后台有没 server 存在, 即 python.exe

# print("stop: {}".format(IN_API_SERVER_MANAGER.stop_server()))



# -------------------- 连接到刚打开的 Local Server --------------------

in_map_dir = 'I:/'

ip, port, username, password, ctype, webserver = '192.168.17.110', 7000, 'root', 'wsrnd', 'DCC', "http://127.0.0.1:20618"


# 在本工程里, src 外有一份 config.json, 里面填写了一些默认值
# IN_API_SERVER_MANAGER 等地方的 webserver 都使用了这些默认值, 所以...
# ip = IN_COMMON.IN_SERVER_IP_ADDRESS
# port = IN_COMMON.IN_SERVER_PORT
# webserver = 'http://%s:%s' % (IN_COMMON.API_SERVER_IP_ADDRESS, IN_COMMON.API_SERVER_PORT)


# 第一次登陆
in_api = InApiClient.connectAndLogin(in_map_dir, ip, port, username, password, ctype, webserver)


# 如果之前已启动过 Server, 并登录过, 那么在其它 DCC, 可以不用再登录
# in_api = InApiClient(in_map_dir, webserver=webserver)

# 在不同的 py 文件, 可直接调用 instance
# in_api = InApiClient.instance()



# -------------------- Examples --------------------
projs = in_api.getProjectFiles()
printer(projs)    # 只是测试打印, 这个 function 可能存在问题, 可自行 print


# proj = in_api.getProject(project_id=88)
# printer(proj)

# files = in_api.listdir(folder_id=12873)
# printer(files)



# -------------------- 如何获取 doc --------------------
# 在其它地方可直接 help(InApiClient)

# 在 Maya 里需要
# import codecs
# for func in dir(InApiClient):
#     doc = eval('InApiClient.%s' % func).__doc__
#     print('-'*60)
#     print func, '\n'
#     if doc:
#         s = codecs.decode(doc, 'utf-8')
#         print s

# files = in_api.listdir(folder_id=13027)
# printer(files)

# ------------------------------ Get ------------------------------
_test_Get = False
if _test_Get:
    projs = in_api.getProjectFiles()
    projs = in_api.getProjects()
    proj = in_api.getProject(217)    # project_id=72
    files = in_api.listdir(folder_id=13027)
    file = in_api.getFileFromId(file_id=4985)
    file_histories = in_api.getFileHistory(file_id=3650)
    file_histories = in_api.getFileHistoryList(task_id=1890)    # 1890, 1891, 1896, 2827, 2829, 2841, 2844, 2862, 2889
    workflow_list = in_api.getWorkFlowTempls(project_id=217, pipeline_type=IN_DATA_STRUCTURE.PipelineType.Shot)
    workflow = in_api.getWorkFlowTempl(workflow_id=2083)
    scenes = in_api.getSceneList(project_id=174)    # 80, 137, 167, 174, 177, 199
    shot = in_api.getShotInfo(shot_id=122)
    person = in_api.getPerson(person_id=20200425)
    people = in_api.getPersonList(department_id=99, team_id=0, filter=0)
    p_steps = in_api.getPipelineSteps(pipeline_type=0, project_id=0)
    placeholder_list = in_api.getPlaceHolderList()
    shots = in_api.getShotsByCondition(project_id=72)    # project_id=72, scene_ids=[65, 61], shot_ids=[533, 534]
    tags = in_api.getTagInfo()    # tag_name="TestTag", tag_object_id=6, resource_id=90
    resources = in_api.getTagResource(tag_name="BonAssetTag_1")
    teams_info = in_api.getTeams(department_id=181)    # department_id=0
    team_info = in_api.getTeam(team_id=400)
    assets = in_api.getAssetsByCondition(project_id=222)    # project_id=72, asset_ids=[435]
    asset = in_api.getAssetInfo(asset_id=947)
    departments = in_api.getDepartments()
    department = in_api.getDepartment(department_id=181)
    tasks = in_api.getTasksByConditions(project_id=217)
    # tasks = in_api.getTasksByConditions(object_ids=[968], type=IN_DATA_STRUCTURE.PipelineType.Asset)
    # tasks = in_api.getTasksByConditions(task_ids=[6603])
    task = in_api.getTaskFromID(task_id=1885)
    file_task_vos = in_api.getTaskFileUsageRecord(task_id=6479, project_id=217, file_type=TaskFileType.All)
    tasks = in_api.getTaskListPersonal(person_id=20200111)
    files = in_api.getTaskRelatedFiles(task_id=6478, file_type=TaskFileType.All)    # return dict: {FileType: `TaskFileVO`}
    # # comments = in_api.getTaskComment(task_id=691)        # TODO: GetTaskComment 的 jsonRequest 返回结果无法解释, 由于IN前端填了错误信息进数据库
    person = in_api.getOneself()
    jobs = in_api.getJobList()
    logs = in_api.getLogs(from_time='2020-4-10 14:13:23')
    storage = in_api.getStorageInfos(project_id=217)
    pass



# ------------------------------ Tag ------------------------------
_test_Tag = False
if _test_Tag:

    tag_name = 'BonAssetTag_2'
    resource_id = 947
    tag_object_id = TagObjectID.Asset    # Folder, Workflow, ...


    # ---------- Make Tag ----------
    # result = in_api.makeTag(tag_name="cgfilm", resource_id=90, tag_object_id=TagObjectID.Folder)           # folder
    result = in_api.makeTag(tag_name=tag_name, resource_id=resource_id, tag_object_id=TagObjectID.Asset)     # asset
    # result = in_api.makeTag(tag_name="TestTag", resource_id=2031, tag_object_id=TagObjectID.Workflow)      # task
    assert result.code == 1


    # ---------- Get Tag ----------
    resources = in_api.getTagResource(tag_name=tag_name)
    print('Get Tag `%s`: %s' % (tag_name, len(resources)))
    printer(resources)


    # ---------- Remove Tag ----------
    result = in_api.removeTag(tag_name=tag_name, resource_id=resource_id, tag_object_id=tag_object_id)
    assert result is True

    resources = in_api.getTagResource(tag_name=tag_name)
    print('Get Tag `%s`: %s' % (tag_name, len(resources)))


# ------------------------ Upload & Download ------------------------
_test_Streaming = False
if _test_Streaming:

    def testUpload():
        # 只限第一次上传文件, 上传后使用 CheckOut

        path = r'I:\BonProject\assets\GG\surfacing\textures\plant\tree\1.jpg'
        folder_id = 5344
        r = in_api.upload(src_path=path, folder_id=folder_id)
        print('upload: ', r)


    def testDownload():
        path = r'I:\demo\s.mp4'
        file_id = 5213
        # 不填 dst_path, 则下载到映射路径下
        r = in_api.download(file_id=file_id, dst_path=None, version=None)
        print('download: ', r)


    def testCheckIn():
        path = r'I:\demo\assets\s.png'
        file_id = 5036
        file = in_api.getFileFromId(file_id=file_id)

        if file.status != IN_DATA_STRUCTURE.FileStatus.CheckOuted:
            raise ValueError('Please Checkout first')

        r = in_api.checkin(file_id=file_id, src_path=path)
        print('checkin: ', r)


    def testCheckOut():
        file_id = 5036
        file = in_api.getFileFromId(file_id=file_id)

        if file.status != IN_DATA_STRUCTURE.FileStatus.CheckIn:
            raise ValueError('Please Checkin first')

        # download=True, checkout 时 可选择是否下载文件
        r = in_api.checkout(file_id=file_id, download=True, version=None)
        print('checkout: ', r)


    def testUploadReference():
        path = u'D:/bon/other/face/小坏坏/3.jpg'
        task_id = 6478

        r = in_api.uploadReferenceFile(task_id=task_id, src_path=path)
        assert r is True

        files = in_api.getTaskRelatedFiles(task_id=task_id, file_type=TaskFileType.Reference)    # return dict: {FileType: `TaskFileVO`}
        for _file_type, task_file_vo in files.items():
            # Here are All References Files
            for file in task_file_vo.files:
                print(file.fileId, file.name)

            for seq_file in task_file_vo.sequenceFiles:
                for file in seq_file.files:
                    print(file.fileId, file.name)


    def testUploadRequired():
        path = u'D:/bon/other/face/小坏坏/3.jpg'
        task_id = 6478

        r = in_api.uploadRequiredFile(task_id=task_id, src_path=path)
        assert r is True


        # result:
        #     {
        #         0: <IN_DATA_STRUCTURE.TaskFileVO object at 0x000000000494EE80>,
        #         1: <IN_DATA_STRUCTURE.TaskFileVO object at 0x000000000494EE80>,
        #         2: <IN_DATA_STRUCTURE.TaskFileVO object at 0x000000000494EE80>,
        #     }

        files = in_api.getTaskRelatedFiles(task_id=task_id, file_type=TaskFileType.Required)    # return dict: {FileType: `TaskFileVO`}
        for _file_type, task_file_vo in files.items():
            # Here are All References Files
            for file in task_file_vo.files:
                print(file.fileId, file.name)

            for seq_file in task_file_vo.sequenceFiles:
                for file in seq_file.files:
                    print(file.fileId, file.name)


    def testUploadOutputFile():
        path = 'I:/BonProject/assets/GG/output/faces/5.jpg'
        task_id = 6478

        r = in_api.uploadOutputFile(task_id=task_id, src_path=path)
        assert r is True

        files = in_api.getTaskRelatedFiles(task_id=task_id, file_type=TaskFileType.Output)    # return dict: {FileType: `TaskFileVO`}
        for _file_type, task_file_vo in files.items():
            for file in task_file_vo.files:
                print(file.fileId, file.name)

            for seq_file in task_file_vo.sequenceFiles:
                for file in seq_file.files:
                    print(file.fileId, file.name)


    def testUploadLibraryFile():
        src_path = u'D:/bon/other/face/小坏坏/11.jpg'
        directory = '/com_1/TEXTURE'

        r = in_api.uploadLibraryFile(src_path, directory=directory, file_name=None)
        assert r is True

        files = in_api.listdir(folder_id=12961)    # library: 12161
        printer(files)


    def testUploadCommentFile():
        path = r'D:\Introduction.mp4'
        task_id = 6478

        r = in_api.uploadCommentFile(
              task_id=task_id, src_path=path,
              comment_type=IN_DATA_STRUCTURE.CommentType.Video)
        assert r is True
        comments = in_api.getTaskComment(task_id)
        for comment in comments:
            print(comment)


    def testUploadPlaceHolders():
        path = r'C:\Users\admin\Desktop\temp.mb'

        r = in_api.uploadPlaceHolders(src_path=path)
        assert r is True

        placeholder_list = in_api.getPlaceHolderList()
        printer(placeholder_list)


    # testUpload()
    # testDownload()
    # testCheckIn()
    # testCheckOut()
    # testUploadReference()
    # testUploadRequired()
    # testUploadOutputFile()
    # testUploadLibraryFile()
    # testUploadCommentFile()
    # testUploadPlaceHolders()


# ------------------------------ Asset ------------------------------
_test_Asset = False
if _test_Asset:

    # ---------- Create Asset ----------
    # 创建 Asset 之后, 会按 workflow 自动创建对应数量的任务
    # 如果你想 Assign Task to Person, 你需要自己获取任务 id, 详见下面 `testEditTask`

    i = 9
    asset_name = 'BonAsset_%s' % i
    project_id, workflow_id, asset_color = 217, 2083, ''
    tags = [ ['my_tag_name', '#ffffff'], ['my_tag_name_2', ''] ] # [ [tag_name, tag_color] ]

    asset_id = in_api.createAsset(
        project_id, workflow_id, asset_name, asset_color,
        description='Created By Python API', tags=tags)
    print('asset_id:', asset_id)


    # ---------- Get Asset Info ----------
    # assets = in_api.getAssetsByCondition(project_id=217)    # project_id=72, asset_ids=[435]
    # asset_id = 963
    asset = in_api.getAssetInfo(asset_id=asset_id)
    printer(asset)


    # And
    # assets = in_api.getAssetsByCondition(project_id=217)    # project_id=72, asset_ids=[435]

    # ---------- Edit Asset ----------
    r = in_api.editAsset(asset_id=asset_id, color='#000000', description='Edit Asset by Python API')
    print('edit asset:', r)


    # ---------- Delete Asset ----------
    # asset_id = 942
    is_successful = in_api.deleteAsset(asset_id)
    print('Delete Asset %s: %s' % (asset_id, is_successful))


# ------------------------------ Scene ------------------------------
_test_Scene = False
if _test_Scene:
    project_id, scene_number = 217, '1'

    scene_id = in_api.createScene(project_id, scene_number)
    print('scene_id:', scene_id)

    # e.g. {'scene_id': 'scene_name'}
    scenes = in_api.getSceneList(project_id=project_id)
    pprint(scenes)
    assert scene_id in scenes


# ------------------------------ Shot ------------------------------
_test_Shot = False
if _test_Shot:
    # ---------- Create Shot ----------
    project_id, workflow_id, scene_number, shot_number, shot_color = 217, 2097, '1', '0300', '#ffffff'
    tags = [ ['my_shot_tag_name', '#ffffff'], ['my_shot_tag_name_2', ''] ]    # [ [tag_name, tag_color] ]

    shot_id = in_api.createShot(
        project_id, workflow_id, scene_number, shot_number,
        shot_color=shot_color, description='Created by Python API', tags=tags)


    # ---------- Get Shot Info ----------
    # e.g. [<INShot>, ...]
    shots = in_api.getShotsByCondition(project_id=project_id, workflow_id=workflow_id)
    # pprint(shots)
    for shot in shots:
        # print(shot.shotId, shot.shotName)
        if shot_id == shot.shotId:
            break
    else:
        raise Exception('Invalid shot_id')

    # And
    # shots = in_api.getShotsByCondition(project_id=72)    # project_id=72, scene_ids=[65, 61], shot_ids=[533, 534]

    # ---------- Edit Shot ----------
    r = in_api.editShot(shot_id=shot_id, color='#000000', description='Edit Asset by Python API')
    print('edit shot:', r)


    # ---------- Delete Shot ----------
    pass


# ------------------------------ Task ------------------------------
_test_Task = False
if _test_Task:

    # -------------------- Get Task Info --------------------
    def testGetTaskInfo(task_id):
        task = in_api.getTaskFromID(task_id)
        # printer(task)
        print('Task:', task.taskId, task.taskName)

        # And
        # tasks = in_api.getTasksByConditions(project_id=217)    # object_ids=[644, 659], task_ids=[5217, 5319, 5320], project_id=72

    # -------------------- Edit Task Info --------------------

    def testEditTask():
        task_id = 6623


        # ----- Edit Task -----
        # 能传入任意参数编辑 Task, 包括 Assign 给某人
        r = in_api.editTask(task_id, color='#ffffff', description='Edited by Python API')
        print('edit task: %s' % r)


        # ----- Assign Task to Person -----
        project_id = 217
        storage_list = in_api.getStorageInfos(project_id=project_id)
        if len(storage_list) == 0: raise ValueError('Invalid Storage Info')
        # 从 storage 里拿到 type, storage_list[0].storageType    # str: hdd

        person_id = 20200480
        team_id = 400
        issue_date = '2020-10-30 00:00:00'
        due_date = '2020-11-08 00:00:00'

        # -----------------------------------------------------
        # 第一次 Assign Task to Person, `需要至少传入下面这几个参数`
        # -----------------------------------------------------
        r = in_api.editTask(
            task_id,
            assignee_team_id=team_id,
            assignee_person_id=person_id,
            storage_type=storage_list[0].storageType,
                # e.g. 'hdd', 创建项目时会要求选一个 storage_type, 默认为 None, 会存储在第一个 storage
            issue_date=issue_date,
                # 开始时间, 需按照具体格式填写
            due_date=due_date
                # 结束时间, 需按照具体格式填写
        )
        print('assign task to person: %s' % r)

    # -------------------- Update Task Status --------------------

    def testToWorkInProgress(task_id):
        # ----- to WorkInProgress -----
        # e.g. 'I:'
        in_map_dir = in_api.getINMapDir()

        # int: 2
        new_status = IN_DATA_STRUCTURE.TaskStatus.WorkInProgress

        # e.g. [2, 9, 10]
        next_statuses = in_api.getTaskNextAvailableStatus(task_id)
        print(next_statuses)

        if new_status not in next_statuses:
            raise ValueError('\n    new_status %s not in NextAvailableStatus %s' % (new_status, next_statuses))

        # 要改为 WorkInProgress, 要先 Checkout 所有 OutputFile
        if new_status == IN_DATA_STRUCTURE.TaskStatus.WorkInProgress:
            # Get output files id & checkout all files
            for file in in_api._getTaskRelatedFiles(task_id, TaskFileType.Output):
                print(file.fileId, file.directory, file.name, file.status)
                if file.status == IN_DATA_STRUCTURE.FileStatus.CheckOuted:
                    continue

                r = in_api.checkout(file.fileId, in_map_dir=in_map_dir)
                print('checkouted:', file.fileId)

        # Update Status
        r = in_api.updateTaskStatus(task_id, new_status, is_required_first_approved=False)
        print('update task status:', r)


    def testToPendingApproval(task_id):
        # ----- to PendingApproval -----
        # e.g. 'I:'
        in_map_dir = in_api.getINMapDir()

        # int: 3
        new_status = IN_DATA_STRUCTURE.TaskStatus.PendingApproval

        # e.g. [3, 9, 10]
        next_statuses = in_api.getTaskNextAvailableStatus(task_id)
        print(next_statuses)

        if new_status not in next_statuses:
            raise ValueError('\n    new_status %s not in NextAvailableStatus %s' % (new_status, next_statuses))

        # 要改为 PendingApproval, 要先 Checkin 所有 OutputFile
        if new_status == IN_DATA_STRUCTURE.TaskStatus.PendingApproval:
            # Get output files id & checkout all files
            for file in in_api._getTaskRelatedFiles(task_id, TaskFileType.Output):

                print(file.fileId, file.directory, file.name, file.status)

                if file.status == IN_DATA_STRUCTURE.FileStatus.CheckIn: continue

                # 文件夹的话需要自己递归, 找出哪些文件需要 upload
                # 上传新 OutputFile 文件需要调用 uploadOutputFile 接口
                # 之前上传过的, 已经在 OutputFile 列表里了
                if file.type == IN_DATA_STRUCTURE.BusFileType.BusEmptyFolderFile: continue

                src_path = in_map_dir + '/'.join([file.directory, file.name])
                print(src_path)
                r = in_api.checkin(file.fileId, src_path=src_path)
                print('checkin:', file.fileId)


        # Update Status
        r = in_api.updateTaskStatus(task_id, new_status, is_required_first_approved=False)
        print('update task status:', r)


    # -------------------- Edit Task Files --------------------

    def testTaskReferenceFile(task_id, file_id):
        # ----- Task Reference File -----

        # Add
        r = in_api.addTaskReferenceFile(task_id, file_id, variant_id=0)
        print('add reference file %s: %s' % (file_id, r))

        # Get
        files = in_api.getTaskRelatedFiles(task_id=task_id, file_type=TaskFileType.Reference)
        pprint(files.values()[0].files + files.values()[0].sequenceFiles)

        # Remove
        r = in_api.removeTaskReferenceFile(task_id, file_id)
        print('remove reference file %s: %s' % (file_id, r))
        return True


    def testTaskRequiredFile(task_id, file_id):
        # ----- Task Required File -----
        # Add
        r = in_api.addTaskRequiredFile(task_id, file_id, variant_id=0)
        print('add required file %s: %s' % (file_id, r))

        # Get
        files = in_api.getTaskRelatedFiles(task_id=task_id, file_type=TaskFileType.Required)
        pprint(files.values()[0].files + files.values()[0].sequenceFiles)

        # Remove
        r = in_api.removeTaskRequiredFile(task_id, file_id)
        print('remove required file %s: %s' % (file_id, r))

        return True


    def testTaskOutputFile(task_id):
        # ----- Task Output & Intermediate File -----


        # 你要添加的 OutputFile 路径
        relpath_n_name = ('/BonProject/assets/GG/geo', 'source.mb')    # e.g. file
        # relpath_n_name = (r'\BonProject\assets\GG\geo', '')    # e.g. folder

        suffix = 'mb'
        placeholder_file_id = None

        # Add
        # 检查你要设置的 OutputFile 路径, 它的后缀, 是否存在于 placeholder list
        # 若不存在, 需要先调用 `uploadPlaceHolders`
        placeholder_files = in_api.getPlaceHolderList()
        for file in placeholder_files:
            if file.name == suffix:
                placeholder_file_id = file.fileId
                break
        else:
            raise ValueError('Please upload placeholder file first')

        # PendingApproval 状态下, 不能添加 OutputFile
        # 这里 Add OutputFile, 仅仅是添加路径, 实际并不上传文件,
        # 注意 relpath_n_name, 是 list/tuple, 是 2 个 elements,
        r = in_api.addTaskOutputFile(task_id, placeholder_file_id, relpath_n_name, is_intermediate_file=False)
        print('add output file, placeholder_file %s: %s' % (placeholder_file_id, r))


        file_id = None
        # Get
        files = in_api._getTaskRelatedFiles(task_id=task_id, file_type=TaskFileType.Output)
        for file in files:
            print(file.fileId, file.directory, file.name, file.status)
            if (file.directory == relpath_n_name[0]) and (file.name == relpath_n_name[1]):
                file_id = file.fileId
                print('\nYour new OutputFile ID: %s' % file_id)
                break
        else:
            raise ValueError('Not found your new OutputFile')

        # Edit
        # Exception: INTERNAL_SERVER_ERROR: Insufficient permissions or other errors
        # r = in_api.editTaskOutputFile(file_id, is_intermediate_file=True)
        # print('edit output file %s: %s' % (file_id, r))

        # Remove
        r = in_api.removeTaskOutputFile(task_id, file_id)
        print('remove output file %s: %s' % (file_id, r))

        return True


    # -------------------- Delete Task --------------------
    def testDeleteTask(task_id):
        # ----- Delete Task -----
        r = in_api.deleteTask(task_id)
        print('delete task: %s' % r)
        return True


    task_id = 6478
    file_id = 5213

    testGetTaskInfo(task_id)
    # testEditTask()
    # testToWorkInProgress(task_id)
    # testToPendingApproval(task_id)
    # testTaskReferenceFile(task_id, file_id)
    # testTaskRequiredFile(task_id, file_id)
    # testTaskOutputFile(task_id)
    # testDeleteTask(task_id)


# ------------------------------ Variant ------------------------------
_test_Variant = False
if _test_Variant:

    asset_id = 947
    variant_name = 'My Variant Created by Python API'

    # ----- Create Variant -----
    variant_id = in_api.createVariant(asset_id, variant_name, file_ids=None)
    print('created variant. id:', variant_id)


    # ----- Get Asset Variant -----
    variants = in_api.getVariantByAssetId(asset_id=asset_id)
    for variant in variants:
        print(variant.variantId, variant.variantName)
        if variant.variantName == variant_name:
            for task_file in variant.taskFiles:
                printer(task_file.files)


    # ----- Edit Variant -----
    variant_name = 'My Variant Edited by Python API'
    r = in_api.editVariant(variant_name)
    print('edit variant:', r)


    # ----- Get Asset Variant Record/Usage -----
    # variants_record = in_api.getVariantRecordByAssetId(asset_id=asset_id)
    # printer(variants_record)


    # ----- Delete Variant -----
    r = in_api.deleteVariantById(variant_id)
    print('delete variant:', r)



# ---------------------------------- My Test ----------------------------------





if __name__ == '__main__':
    pass

